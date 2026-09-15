import sys

def replace_with_opacity(text):
    out = []
    i = 0
    while i < len(text):
        idx = text.find('.withOpacity(', i)
        if idx == -1:
            out.append(text[i:])
            break
        
        out.append(text[i:idx])
        out.append('.withValues(alpha: ')
        i = idx + 13
        
        paren_count = 1
        start_val = i
        while i < len(text) and paren_count > 0:
            if text[i] == '(':
                paren_count += 1
            elif text[i] == ')':
                paren_count -= 1
                if paren_count == 0:
                    out.append(text[start_val:i])
                    out.append(')')
                    i += 1
                    break
            i += 1
            
    return ''.join(out)

for fpath in ['lib/splash_screen.dart', 'lib/home_screen.dart']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = replace_with_opacity(content)
    content = content.replace('_, __, ___', 'context, animation, secondaryAnimation')
    content = content.replace('_, animation, __', 'context, animation, secondaryAnimation')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done fixing")
