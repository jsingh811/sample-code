import java.util.*;
import java.io.*;
import java.net.*;
import java.lang.Object;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;

public class PageTagger 
{
	public int len = 0;
	public String main_text_web = "";
	public String tagged_text_web = "";
	int max_len = 10000;
	int delim_len = 200;
	MaxentTagger tagger = new MaxentTagger("models/english-left3words-distsim.tagger");

	public String getText(URL adr) throws IOException
	{
		String temp_str;
		StringBuilder builder = new StringBuilder();
        BufferedReader in = new BufferedReader(new InputStreamReader(adr.openStream()));
        
		//convert bufferreader into string
		while ((temp_str = in.readLine()) != null) 
		{
			builder.append(" " + temp_str);
		}
		
        String web_text = builder.toString();
		//get body of webpage
		Document doc = Jsoup.parse(web_text);
		main_text_web = doc.body().text();
		len = main_text_web.length();
		return main_text_web;
    }
		
	
	//method for tagging text
	public String tagText(String webtxt)
	{
		int flag = 0;
		int start_index = 0;
		int end_index = 0;
		String part = "";
		
		//checking if length of string is less than 10000
		if(len < max_len)
		{
			String tagged = tagger.tagString(webtxt);
			tagged_text_web = tagged;
		}
		
		else// if length of string is greater than 10000, we break the string into subparts and get the tagging output
		{
			end_index = max_len;
			int temp = end_index;
		
			while(start_index < len)
			{
				temp = end_index;
				flag = 0;
			
				// to check that the index where we break string at is the end of a sentence,if there exists one, for proper tagging
				// we check for at max 200 characters to encounter end of sentence. If it does not detect one, we break the sentence using space.
				while((temp < len) && (flag < delim_len) && !(webtxt.substring(temp-1 , temp)).matches("[.!?]"))
				{ 
					temp++;
					flag++;
				}
					 
				if(flag == delim_len)
				{
					temp = temp - delim_len;
				
					while((temp < len) && !(webtxt.substring(temp-1 , temp)).equals(" "))
					{
						temp++;
					}
				}
				end_index = temp;							
				part = webtxt.substring(start_index , end_index);//substring
				String tagged = tagger.tagString(part);//tagging
				tagged_text_web = tagged_text_web + tagged;
				start_index = end_index;
				end_index = end_index + max_len;
				
				if(end_index > len)// ensuring index doesn't go out of bounds
					end_index = len;
			}
		}
		return tagged_text_web;
	}
	
	
	//method for displaying
	public void disp(String str)
	{
		System.out.println(str);
	}
	
	public static void main(String[] args) throws IOException
	{	
		int exception_flag = 0;
		String web_add;
		String web_text="";
		String tagged_text="";
		Scanner input = new Scanner(System.in);
		PageTagger obj = new PageTagger(); //Creating object of class PageTagger
		
		do
		{
			try 
			{
				System.out.print("Enter the web address: ");
				web_add = input.next( );
				URL adr = new URL(web_add);
				web_text=obj.getText(adr);//calling method getText
				tagged_text=obj.tagText(web_text);//calling method tagText
				obj.disp("Tagged output of the text: ");
				obj.disp(tagged_text);
				//Check if user wants to tag more webpages
				do
					{
						obj.disp("\n More webpages to tag? Y/N :");
						String localstr=input.next();
						if(localstr.equals("N"))
							exception_flag = 0;
						else if(localstr.equals("Y"))
							exception_flag=1;
						else
							{
								System.out.println("Invalid entry. ");
								exception_flag=100;
							}
					}
				while(exception_flag==100);
				
			}
			// user gets the chance to input web address again if an invalid one is passed as an input earlier
			catch(Exception exp)
			{
				if( exp instanceof MalformedURLException || exp instanceof IllegalArgumentException || exp instanceof FileNotFoundException )
				{
					exception_flag = 1;
					obj.disp("Invalid entry. ");
				}
			}
		}
		while(exception_flag == 1);
		
		input.close();		
	}//end main
}