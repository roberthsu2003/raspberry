## 安裝python軟體工具和建立虛擬環境
- [安裝python3.x](#install_python)
- [安裝condamini和jupyter(要用jupyter一定必需使用condamini)](#安裝condamini和jupyter)
- [使用Conda建立python的虛擬環境](#使用Conda建立python的虛擬環境)
- [使用virtualEnv建立python虛擬環境](#使用virtualEnv建立python虛擬環境)

<a name="install_python"></a>
## 安裝python 3.x

### 檢查目前預設python,python3版本
`$ python --version`

`$ python3 --version`

### 檢查執行那一個python
`$ which python`

`$ which python3`

### 安裝python3

```
$ sudo apt update
$ sudo apt install python3
```


<a name=“install_python”></a>
## 安裝python

```
#檢查python版本
$ python —version

#目前python的路徑
$ which python

#安裝python3
$ sudo apt-get inatll python3

#更改環境設定
$ sudo vim ~/.bashrc
# 在最後一行加上
export PATH=“/usr/bin:$PATH”
```


<a name="安裝condamini和jupyter"></a>
## 安裝miniconda和jupyter

### 步驟 1:下載miniconda
	$ wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh

### 步驟2:安裝miniconda
一開始會出現License ，一直按enter會出現問你是否同意Licence，輸入yes。

會問你要安裝在預設路徑 /root/minconda3，或其他地方。我是安裝到此處:
/home/pi/miniconda3

會問你要不要加入PATH，先輸入no，下步驟再加入PATH

	$ sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh
	
### 步驟3:設定PATH

	$ sudo nano /home/pi/.bashrc

在檔案最尾端加入下方文字後存檔

	export PATH=”/home/pi/miniconda3/bin:$PATH”
	
重新執行.bashrc

	$ source ~/.bashrc
	
步驟4:更改miniconda3下的所有檔案及目錄，為pi的擁有者

	$ sudo chown -R pi miniconda3
	
步驟 5:安裝python，會問是否同意安裝，按y

	#修改conda的預設檔,告知要使用的硬體是rpi
	conda config —add channels rpi
	
	#查詢conda提供的python版本 conda search "^python$"
	conda install python=3.6
	
步驟 6:安裝Jupyter notebook

	$ conda install jupyter
	
步驟 7:測試

	$ python -V
	$ which python
	
步驟 8:開啟jupyter

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