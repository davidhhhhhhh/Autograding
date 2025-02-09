# **Autograding: Student Simulator for Fine-Tuning Models**

## **Introduction**
This repository implements a **student simulator** to fine-tune a **large language model** (LLM) and **large vision model** (LVM) for grading student answers. 

The student simulator is built on probabilistic programming principles to simulate **students' decision-making processes**. For more details on the **student simulator** and task descriptions, refer to the following paper:  
[Simulated Students for Automated Grading](https://arxiv.org/abs/1905.09916).

---

## **Requirements**
Ensure you have the following dependencies installed:

### **Python**
```sh
python --version
Python 3.11.9
```

### **Java**
```sh
java -version
java version "22.0.2" 2024-07-16
Java(TM) SE Runtime Environment (build 22.0.2+9-70)
Java HotSpot(TM) 64-Bit Server VM (build 22.0.2+9-70, mixed mode, sharing)
```

### **Java Compiler (Javac)**
```sh
javac -version
javac 22.0.2
```

---

## **Usage**
This repository supports generating both **natural language** and **image** data.

### **1. Generating Natural Language Data**
To generate text-based student responses:

```sh
cd StudentSimulator/generate
python powerSample.py
```
or
```sh
python javaSample.py
```
- Modify the **loop parameters** inside the scripts to control the number of samples generated.
- The output will be saved in **CSV format**.

---

### **2. Generating Image Data**
To generate **image-based** student responses:

```sh
cd StudentSimulator/generate
python pyramidSample.py
```
or
```sh
python pyramidSampleKS.py
```
- The output is saved in **JSON format**.
- `pyramidSampleKS.py` generates images based on different **knowledge components**.

---

### **3. Converting Java Scripts to Images**
To convert the **generated Java scripts** into images:

```sh
cd StudentSimulator/generate/ImageGenerator/imagesByKs
mv ../sampled/*.json .
```
- Modify the **root directory** in `json2PngKs.py` to your local path.
- Run the script to generate images:
  ```sh
  python json2png.py
  ```
- The output will be saved in **corresponding subfolders**.

---

### **4. Modifying the Decision Nodes & Probabilities**
- All generated data follow **prewritten grammars**.
- To modify **decision nodes** or **probability distributions**, edit the grammars in:
  ```
  StudentSimulator/generate/grammars/
  ```

---

## **Model Fine-Tuning**
- **Colab** is used for **fine-tuning models**.
- For model training details, check the **Jupyter notebooks** in the `model/` directory.

---

## **Contact**
For any questions or collaboration inquiries, please reach out to:  
📧 **dkosmos1774@gmail.com**  
📌 **David Dai**