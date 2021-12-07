# GraphManager

## Installation 

1. Download [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html).
  
2. Create a new environment:
    ```
    conda create -n [ENV_NAME] python=3.7
    conda activate [ENV_NAME]
    ```
   
5. Install GraphManager
    ```
    cd ~
    git clone https://github.com/lsorgi/GraphManager.git
    cd GraphManager
    pip install -e .
    ```

## Run tests 
   
```
cd ~/GraphManager
pytest ./tests 
```
