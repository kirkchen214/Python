# Python 学习记录

保留原知识点、变量名和练习顺序，补充说明、输出结果与易错点。

| 阶段 | 文件 | 内容 |
| --- | --- | --- |
| 第一次学习 | [hello_world.py](hello_world.py) | 第一个程序 |
| 第一次学习 | [constant_variable.py](constant_variable.py) | 变量、类型、字符串和输入 |
| 复习练习 | [day_test.py](day_test.py) | 输入机器人名称与电量，电量增加 5 |
| 第二次学习 | [operators_demo.py](operators_demo.py) | 七种算术运算 |
| 第二次学习 | [if_else.py](if_else.py) | 先判断正负数，再执行四则计算器 |
| 学习笔记 | [学习文档.md](学习文档.md) | 第 1～7 节为原笔记，第 8 节起为新增内容 |

## 在 Ubuntu 中运行

进入项目目录，先检查版本：`match/case` 要求 Python 3.10 或更高版本。

```bash
python3 --version
python3 hello_world.py
python3 constant_variable.py
python3 day_test.py
python3 operators_demo.py
python3 if_else.py
```

逐条运行；程序出现输入提示时，输入内容后按 Enter。
`if_else.py` 一共输入四次：`num`（整数）、`num1`、`num2`（普通有限数值）、`operator`（`+ - * /` 之一）。例如依次输入 `5`、`10`、`4`、`/`，会输出正数判断和 `10.0/4.0=2.5`。
数值输入暂不处理空字符串和非数字文本，异常处理留到后续章节。

若已激活 `.venv`，也可以使用 `python`。本次代码不需要第三方库。

## 文件名与缓存

原 `operator.py` 改为 `operators_demo.py`，避免与 Python 标准库 `operator` 重名；原七个算式全部保留。
`__pycache__` 中的 `.pyc` 是自动生成的缓存，不是学习源码。本次移除已提交的缓存，并通过 `.gitignore` 忽略后续生成的文件。
