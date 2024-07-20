## 安裝python軟體工具和建立虛擬環境
- [安裝miniforge和jupyter(要用jupyter一定必需使用miniforge)](#安裝miniforge和jupyter)
- [使用Conda建立python的虛擬環境](#使用Conda建立python的虛擬環境)

<a name="安裝miniforge和jupyter"></a>
## 安裝miniforge和jupyter

### 步驟 1:下載miniforge
`wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh`

### 步驟2:安裝miniforge

`/bin/bash Miniforge3-Linux-aarch64.sh`

一開始會出現License ，一直按enter會出現問你是否同意Licence，輸入yes。


會問你要不要加入PATH，先輸入no，下步驟再加入PATH


	
### 步驟3:設定PATH

`nano /home/pi/.bashrc`

在檔案最尾端加入下方文字後存檔

`export PATH="/home/pi/miniforge3/bin:$PATH"`
	
重新執行.bashrc

`$ source ~/.bashrc`
	
步驟 4:

```
conda init --all bash
```	

步驟 5:安裝Jupyter notebook

	$ conda install jupyter
	
步驟 6:測試

	$ python -V
	$ which python
	
步驟 7:開啟jupyter

	$jupyter notebook
	
<a name="使用Conda建立python的虛擬環境"></a>
## 使用Conda建立python的虛擬環境
- 安裝numpy, pandas, matplotlib
- 安裝gpio套件

### 1.檢查conda版本
	$ conda -V
	conda 4.5.11
	
### 2.更新conda
	$ conda update conda
	
### 3.建立python虛擬環境
	#檢查conda提供的python版本
	$ conda search "^python$" 
	
	#建立一個虛擬環境env01, x.x為要安裝的版本
	$ conda create -n env01 python=x.x
	
### 4.啟動conda虛擬環境

	$ source activate env01

	#查看目前所有conda的虛擬環境
	conda info -e
	
### 5.使用conda安裝python package
	$ conda install -n env01 numpy
	$ conda install -n env01 pandas
	$ conda install -n env01 matplotlib
	

### 6.離開conda的虛擬環境
	$source deactivate
	
### 7. 刪除虛擬環境
	$ conda remove -n env01 -all

 <a name="使用virtualEnv建立python虛擬環境"></a> 
## 使用virtualEnv建立python虛擬環境

### 1. 安裝virtualEnv

```
$ pip3 install --upgrade pip
$ pip3 install virtualenv
```

### 2. 建立虛擬環境

- 建立在個人根目錄

```
$ cd ~
pi@raspberrypi:~ $ virtualenv venv
```

### 3. 啟動虛擬環境

```
pi@raspberrypi:~ $ source ./venv/bin/activate

結果:===================
(venv)pi@raspberrypi:~ $
```

### 4. 離開虛擬環境

```
(venv)pi@raspberrypi:~ $ deactivate

結果:=====================
pi@raspberrypi:~
```

### 5. 遷移虛擬環境

- 先將全部相依函式庫輸出到requirements.txt內

```
(venv)pi@raspberrypi:~ $pip3 freeze > requirements.txt
```

- 內將全部相依函式庫安裝到別的環境

```
(venv01)pi@raspberrypi:~ $pip3 -r requirements.txt
```
