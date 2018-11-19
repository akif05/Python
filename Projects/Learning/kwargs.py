def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result +='>'
    return result

res = tag('img', src="monet.jpg", alt="sunrizeadfa adfa", border=1)

print(res)
