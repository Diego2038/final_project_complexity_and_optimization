# Final proyect of complexity and optimization

The project is about planning energy production to meet customer demand, with the aim of maximizing net profit. A model must be implemented in MiniZinc that considers production costs, plant capacities, customer demand and payments per MW.
This application configures the parameters and executes the model, in order to observe the most optimal results according to the aforementioned criteria.

## Pre requirements

Before you begin, make sure you have Python installed on your system. You will also need MiniZinc for some of the app's functionality. You can check if MiniZinc is installed by running:

```bash
minizinc --version
``` 
If a message does not appear with the version of Minizinc, it means that you must install Minizinc, as well as establish it in the environment variables.



## Virtual Environment Configuration
It is advisable to use a virtual environment to install the necessary libraries and keep your development environment isolated. To create and activate a virtual environment, follow these steps:

### 1. Create a virtual environment with the next command: 
If you're in Windows
```bash
python -m venv venv
```
If you're in Linux or MacOs:
```bash
python3 -m venv venv
```

### 2. Activate the virtual environment through the following command:

If you're in Windows
```bash
.\venv\Script\activate
```
If you're in Linux or MacOs:
```bash
source venv/bin/activate
```

### 3. With the virtual environment activated, install the dependencies by running:

If you're in Windows:
```bash
pip install -r requirements.txt
```
If you're in Linux or MacOs:
```bash
pip3 install -r requirements.txt
```

This will install all the necessary Python libraries that are defined in the requirements.txt file.

## Application Execution
Once you have configured your environment and verified the installation of MiniZinc, you can run the application with the following command:
```bash
python gui.py
```

## Functioning
It is only necessary to fill in the fields of the requested variables located in the user interface, it can be inserted manually as well as upload a .dzn file as in the examples located in the "PlantaFuentes" folder.

If you want to load a .dzn file, you just have to click on the "Load file" button.
To see the results returned by the model, click on the "Submit" button, you will immediately see a pop-up window with the respective responses.
In the event that the information of the variables in the .dzn file or the fields of the graphical interface are not filled in correctly, a pop-up message will appear that will warn you of this inconsistency.


## Contributions
- [miguelVillaq](https://github.com/miguelVillaq)
- [jorgeasmz](https://github.com/jorgeasmz)
- [Diego2038](https://github.com/Diego2038)