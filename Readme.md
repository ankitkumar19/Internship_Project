# **Web Automation Framework**

## Input files 

*1. Json file containing the base url and the steps required for automation.*

```json
{
	"base_url" : "https://protonmail.com/",
	"steps": [
		{
			"number": 1, // the step no. (Should be unique)
			"xpath": "/html/body/div[1]/nav/div[2]/div/div[2]/ul/li[8]/a", //attribute to identify																	 element (xpath,id,etc)
			"wait": 10, // amount of time the web driver should wait before performing thr req.					 operation
			"operation": "CLICK"// the type of operation to be performed on the element
		}
	]
}
```

*2. Json file containing the data required for automation.*
```json
{
	"obj1":[
		{
			"value":[								// Arrays of data that is to be entered into 												the  required fields in the order in which 												they are required. 
				"abcdefgh@protonmail.com",
				"abcdefgh",
				"xyz@gmail.com",
				"Automated hello"
			]
		}
	],
	"method" : "xpath"// Type of attribute to be used to identify element
}	
```

## Output

*The tasks specified in the json files are automated files are automated by following the mentioned state*