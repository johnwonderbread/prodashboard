# importing requests package 
import requests	 

def TopUsNews(): 
	
	# BBC news api 
	main_url = " https://newsapi.org/v2/top-headlines?country=us&apiKey="

	# fetching data in json format 
	open_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_page["articles"] 

	# empty list which will 
	# contain all trending news 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
		
		# printing all trending news 
		print(i + 1, results[i])				 

# Driver Code 
if __name__ == '__main__': 
	
	# function call 
	TopUsNews() 
