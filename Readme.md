# Data Retrival API

## Usage

All responses will have the form

```json 
{
	"data" : "Mixed type holding the content of response",
	"message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all files that need automation

**Definition**

`GET /filedir`

**Response**

- `200 OK` on success

```json
{
	"filedir" : [
		"file1.json",
		"file2.json",
	],
	"datadir": [
		"file1_data.json",
		"file2_data.json"
	]
}
```

### Adding a new file

**Definition**

`POST /filedir`
 
**Arguments**

-- `"filedir" : string` path of the file containing the steps for automation
-- `"datadir" : string` path of the file conatining thre data for automation

**Response**

--`201 Created` on successs

```json
{
	"filedir" : [
		"file1.json",
		"file2.json",
	],
	"datadir": [
		"file1_data.json",
		"file2_data.json"
	]
}
```
### Lookup automation files

`GET /filedir/file.json`

-- `404 Not Found` if the device does not exist
-- `200 OK` on success

```json
{
	"base_url": "https://protonmail.com/",
	"steps": [
		{
			"number": 1,
			"xpath": "/html/body/div[1]/nav/div[2]/div/div[2]/ul/li[8]/a",
			"wait": 10,
			"operation": "CLICK"
		},
		{
			"number": 2,
			"xpath": "/html/body/div[2]/div[1]/div/div/form/div[1]/input",
			"wait": 10,
			"operation": "SEND_KEYS"
		}
	]
}
```

### Adding a new step

**Definition**

`POST /filedir/file.json/[steps]`
 
**Arguments**

-- `"number" : integer` unique step number
-- `"xpath" : string` xpath of the element to be selected
-- `"wait": integer` amount of time the web driver is supposed to wait
-- `"operation" : string` type of operation to be performed on the selected element

**Response**

--`201 Created` on successs

```json
{
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

### Lookup data files

`GET /filedir/file_data.json`

-- `404 Not Found` if the device does not exist
-- `200 OK` on success

```json
{
	"obj1": [
		{
			"value": ["/home/ankit/project/automate1.py"]
		},
		{
			"value": ["/home/ankit/project/scrapping1.py"]
		}
	],
	"method": "xpath"
}
```