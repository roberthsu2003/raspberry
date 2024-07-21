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
	
<a name="使用Conda建立python的虛擬環境"></a>
## 取消termail一開始就進入base虛擬環境

```
conda config --set auto_activate_base false
```

## conda init

```
conda init --all bash
```

## conda版本檢查

```
conda -V
```

## conda更新

```
conda update conda
```

## 檢查目前已建立的虛擬環境

```
conda env list
```

## 建立虛擬環境

```
conda create --name myenv python=3.10
```

## 啟動虛擬環境

```
conda activate myenv
```

## 離開虛擬環境

```
conda deactivate
```

## 安裝套件

```
conda activate myenv
conda install matplotlib
```

```
conda install --name myenv matplotlib
```

## 安裝requirement.txt

```
conda install --yes --file requirements.txt
```

## 檢查目前安裝的套件

```
conda list
```
## 刪除虛擬環境

```
conda env remove --name myenv
```

## 刪除虛擬環境的套件

```
conda remove --name myenv matplotlib
```

