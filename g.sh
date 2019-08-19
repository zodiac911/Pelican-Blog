# 自动生成博客文件并同步至 Github

source activate pelican # 激活环境
pelican content -s publishconf.py -o output/blog # 生成 html
#ghp-import output -b master # 将 output 中的文件添加进 master 分支
cd output
git add -A
git commit -m /
git push origin master # push 到远端