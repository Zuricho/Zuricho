# Git

## 最常用流程

```bash
git clone [link]
# 平时推荐使用https
# 如果https clone下来的库没法push，可以换用git链接试试
```

```bash
git add .
git commit -m "commit note"
git push origin master
```



## 创建版本库

```bash
git init
git add [filename]    # 把要提交的所有修改放到暂存区 (Stage)
git commit -m "commit note"   # 一次性把暂存区的所有修改提交到分支
```



## 常用git指令

```bash
git status   # 找到修改过的文件

git diff [filename]  # diff

git log   # 显示从最近到最远的提交日志

git reset --hard HEAD^  # 回退到上一个版本

git reset --hard 1094a   # 回退到某个具体版本

git rm [filename]
```

## 添加远程仓库

```bash
git remote add origin git@github.com:Zuricho/[repoName].git
```

添加后，远程库的名字就是origin，这是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库。

```bash
git push -u origin master

git push origin master
```

由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。

```bash
git remote -v   # 查看远程库信息

git remote rm origin  # 删除远程库

git clone git@github.com:Zuricho/DeepAccNet.git   # 克隆到本地
```

## 分支管理

```bash
git checkout -b dev   # 创建并转换到dev分支

git branch dev        # 创建dev分支
git checkout dev      # 转换到dev分支（不推荐）
git switch -c dev     # 转换到dev分支（新版）

git branch            # 列出所有分支

git add [filename]
git commit -m "branch test" 

git merge dev         # 合并分支

git branch -d dev     # 删除分支

git log --graph       # 看到分支合并图
```

读到了这里 [Link](https://www.liaoxuefeng.com/wiki/896043488029600/900005860592480)



[Another Reference for Git branch control: TortoiseGit升级操作说明](https://blog.csdn.net/cy309173854/article/details/52621185)