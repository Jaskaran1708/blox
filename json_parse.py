def parse_json(str):
    def parse_value(i):
        i = skip_whitespace(str, i)
        char = str[i]

        if char == '"':
            return parse_string(str, i)
        elif char == '{':
            return parse_object(str, i)
        elif char == '[':
            return parse_array(str, i)
        elif char.isdigit():
            return parse_number(str, i)
        elif str[i:i + 4] == 'true':
            return True, i + 4
        elif str[i:i + 5] == 'false':
            return False, i + 5
        elif str[i:i + 4] == 'null':
            return None, i + 4

    def parse_string(s, i):
        i += 1  
        result = ""
        while s[i] != '"':
            result += s[i]
            i += 1
        return result, i + 1 

    def parse_number(s, i):
        num_str = ""
        while i < len(s) and (s[i].isdigit() or s[i] in '-.'):
            num_str += s[i]
            i += 1
        if '.' in num_str:
            return float(num_str), i
        else:
            return int(num_str), i

    def parse_object(s, i):
        result = {}
        i += 1 
        while s[i] != '}':
            i = skip_whitespace(s, i)
            key, i = parse_string(s, i)
            i = skip_whitespace(s, i + 1)  
            value, i = parse_value(i)
            result[key] = value
            i = skip_whitespace(s, i)
            if s[i] == ',':
                i += 1 
        return result, i + 1  

    def parse_array(s, i):
        result = []
        i += 1  
        while s[i] != ']':
            i = skip_whitespace(s, i)
            value, i = parse_value(i)
            result.append(value)
            i = skip_whitespace(s, i)
            if s[i] == ',':
                i += 1  
        return result, i + 1  

    def skip_whitespace(s, i):
        while i < len(s) and s[i] in ' \n\t\r':
            i += 1
        return i

    result, _ = parse_value(0)
    return result

json_string = '{"name": "John", "age": 30, "is_student": false, "balance": 12345.67, "hobbies": ["reading", "sports"], "address": null}'
result = parse_json(json_string)
print(result)
