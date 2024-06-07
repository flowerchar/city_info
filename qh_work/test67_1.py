def filter_chars(s):
    """
    过滤掉字符串中的非英文字母字符

    参数:
    s (str): 输入字符串

    返回:
    str: 只包含英文字母的字符串
    """
    filtered_string = ''.join(char for char in s if ('a' <= char <= 'z' or 'A' <= char <= 'Z'))
    return filtered_string

# 示例使用
input_str = "Hello, World!大声道· 123@#$"
filtered_str = filter_chars(input_str)
print(filtered_str)  # 输出: HelloWorld
