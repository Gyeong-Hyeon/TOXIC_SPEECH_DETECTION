import re
import unicodedata

def clean_text(text):
    text = text.lower().strip()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[\r|\t|\n]', ' ', text)
    text = re.sub('(http|ftp|https)://(?:[-\w.]|(?:\da-f]{2}))+','',text) #url 제거
    text = re.sub('(\[a-z0-9\_.+-\]+@\[a-z0-9-\]+.\[a-z0-9-.\]+)','',text) #email 제거
    text = re.sub('<[^>]*>','',text) #html tag 제거
    text = re.sub(r"([.!?])", r" \1", text) #문장부호는 \1로 대체
    text = re.sub(r"[^a-z.!?]+", r" ", text) #문자+문장부호만 빼고 모두 제거
    text = re.sub(' the ', ' ', text)
    text = re.sub(' a ', ' ', text)
    text = re.sub(' u ', 'you ', text)
    text = re.sub(' ur ', ' your ', text)
    text = re.sub(' y ', 'why ', text)
    text = re.sub(' ciu ', 'see you ', text)
    text = re.sub(' da ', 'dumb ass ', text)
    text = re.sub(' fug ', 'fuck ugly ', text)
    text = re.sub('gratest', 'greatest ', text)
    text = re.sub('sh\*t', 'shit ', text)
    text = re.sub('s\*\*t', 'shit ', text)
    text = re.sub('f\*ck', 'fuck ', text)
    text = re.sub(' f ', 'fuck ', text)
    text = re.sub('fu\*k', 'fuck ', text)
    text = re.sub('f\*\*k', 'fuck ', text)   
    text = re.sub('f\*\*\*\*\*g', 'fuck ', text)
    text = re.sub('p\*ssy', 'pussy ', text)
    text = re.sub('p\*\*\*y', 'pussy ', text)
    text = re.sub('pu\*\*y', 'pussy ', text)
    text = re.sub('p\*ss', 'piss ', text)
    text = re.sub('b\*tch', 'bitch ', text)
    text = re.sub('bit\*h', 'bitch ', text)
    text = re.sub(' btch ', 'bitch ', text)
    text = re.sub(' bch ', 'bitch ', text)
    text = re.sub('h\*ll', 'hell ', text)
    text = re.sub('h\*\*l', 'hell ', text)
    text = re.sub('cr\*p', 'crap ', text)
    text = re.sub('d\*mn', 'damn ', text)
    text = re.sub('stu\*pid', 'stupid ', text)
    text = re.sub('st\*pid', 'stupid ', text)
    text = re.sub('n\*gger', 'nigger ', text)
    text = re.sub('n\*\*\*ga', 'nigger ', text)
    text = re.sub('f\*ggot', 'faggot ', text)
    text = re.sub('scr\*w', 'screw ', text)
    text = re.sub('pr\*ck', 'prick ', text)
    text = re.sub('g\*d', 'god ', text)
    text = re.sub('s\*x', 'sex ', text)
    text = re.sub('a\*s', 'ass ', text)
    text = re.sub('a\*\*hole', 'asshole ', text)
    text = re.sub('a\*\*\*ole', 'asshole ', text)
    text = re.sub('a\*\*', 'ass ', text)    
    text = re.sub(r"im ", "i am ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    
    return text

def preprocessing(comment):
    if type(comment) == str:
        return [clean_text(comment)]
    elif type(comment) == list:
        comments = []
        for text in comment:
            text = clean_text(text)
            comments.append(text)
        return [' [SEP] '.join(comments)]