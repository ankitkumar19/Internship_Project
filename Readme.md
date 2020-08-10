# **Web Automation Framework**

## Input files 

*1. Json file containing the base url and the steps required for automation.*

```json
{
	"base_url" : "https://protonmail.com/",
	"steps": [
		{
			"number": 1, 
			"xpath": "/html/body/div[1]/nav/div[2]/div/div[2]/ul/li[8]/a", 
			"wait": 10, 
			"operation": "CLICK"
		}
	]
}
```
*number* : The step number. (Should be unique)
*xpath* : Attribute to identify element. (xpath,id,etc)
*wait* : Amount of time the web driver should wait before performing the required operation.
*operation* : The type of operation to be performed on the element.


*2. Json file containing the data required for automation.*
```json
{
	"obj1":[
		{
			"value":[								
				"abcdefgh@protonmail.com",
				"abcdefgh",
				"xyz@gmail.com",
				"Automated hello"
			]
		}
	],
	"method" : "xpath"
}	
```
*value* : Arrays of data that is to be entered into the required fields in the order in which they			  are required.
*method* : Type of attribute to be used to identify element.



## Output

*The tasks specified in the json files are automated files are automated by following the mentioned state*