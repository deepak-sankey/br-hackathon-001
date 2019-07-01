# BR Hackathon 001

A new organisation has decided to base their company logo on the three most common characters in the company name. Given a string ,which is the company name, your task is to find the top three most common characters in the string. If the occurrence count is the same, sort the characters in alphabetical order.
    For example, according to the conditions described above,
    YAHOO would have it's logo with the letters O, A, H.
    
Note:
1. The problem statement must be exposed as an REST API
2. A JSON file of company ID and company name is attached with the problem statement. Store it in your file system.
3. The REST API will accept company ID as a input, fetch the name from JSON file, and will return company Id, company Name and logo characters as output.
    > I/P : {companyId: "C001"}
    > O/P: {companyId:"C001" , companyName:"YAHOO",logoCharacters:"O,A,H"}
4. Use python as your programming language. Flask will be used as Web API. Coding standards and code design should be followed and will be considered for assessment will along with logic and output.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

* **Deepak Terse** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
