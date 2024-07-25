# research_2024
This is a repository that aims to create student simulators described by Ali Malik. The paper details can be accessed in below link: https://arxiv.org/abs/1905.09916

In side Idea2Text/part1-starter/generate/grammars, you can find simulators for powergrading and pyramid challenge. For specifics on the simulator, please refer to the original paper. To revise outputs from these simulators, you should only change corresponding decision nodes in respective directories. 

To generate output for powergrading, run powerSample.py file located in Idea2Text/part1-starter/generate. For it to run successfully, please set generate directory as the base directory. The output will be a csv file. 

To generate outputpr for pyramid challenge, it is a bit complicated. First, you need to run pyramidSample.py file which will generate a json file containing the number of pictures you wish to generate. Then you need to put the json file into Imagegenerator/test folder and run javaCreation.py to create corresponding java files. You will then run the shell script compile_java_files.sh and run_java_files.sh to generate images. 
