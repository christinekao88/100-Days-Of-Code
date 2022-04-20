# 100 Days of Code
> 100 Days of Code - The Complete Python Pro Bootcamp for 2021

###### tags: `Python` 

## Day 1 : Strings
* print( ) function : `print("hello")`
* Strings concatenation : `print("hello"+"world")`
* input( ) function -> always get str
* variable

## Day 2 : Data Type
* Data type
    * strings
        * subscript : `print("hello"[0])` 
            > computer count from 0 
    * integer
        * larger integer : 123456 -> `123_456`
            > computer will ingnore '_'
    * float
    * boolean 
* type( ) function
* Mathematical Operations
    * `6 / 3 -> 2.0 (float)` (division得到float)
    * `2**3` (2的3次方)

* 運算準則PEMDAS分別是： 
    * Parentheses（括號）: `()`
    * Exponents（指數）: `**`
    * Multiplication（乘法）: `*`
    * Division（除法）: `\`
    * Addition（加法）: `+`
    * Subtraction（減法）: `-`

* Number Manipulation
    * round() function : `round(8/3 , 2) -> 2.67`
    * `8//3 -> 2 (int)` (The result of the integer division
)
    * `4//2 -> 2 (int)` (The result of the float division
)
    * `4/2 -> 2 (float)`

* F String

## Day 3 : Conditional 
* Conditional 
    * If/Else
    * Nested If/Else
    * If/Elif/Else ->只有一個條件會被執行
    * Multiple IF -> 三個IF條件都會執行

* Comparison Operators  
* Logical Operators  
    * A AND B
    * A OR B
    * NOT A 


## Day 4 : Data Structure

* Randomisation
* Deterministic
* pseudorandom number generator 偽隨機數
    * python用的方法是Mersenne Twister

        > https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators     
         
        > https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences


* Module:
    * random 

* Data Structure : Python儲存數據的一種方式
    > https://docs.python.org/3/tutorial/datastructures.html

* Lists
    ```=python
    b=[]

    b.insert(1,5) # 用于将指定对象插入列表的指定位置

    b.insert(1,10) # 將10放到1的位置

    b.insert(0,6)

    print(b) # [6, 5, 10]


    b.remove(6)

    b.append(9)

    b.append(1)

    b.sort() # 用于对原列表进行排序

    print(b) # [1, 5, 9, 10]


    b.pop() # 移除列表中的一个元素（默认最后一个元素）

    b.reverse() # 反向列表中元素

    print(b) # [9, 5, 1]
    ```

## Day 5 : Loops

* For Loops
    ```=python
    for item in list_of_items:
        print('Do sth in each item')
    ```
* Range( ) function
    ```=python
    for number in range(a,b):
        print(number)
     ```
## Day 6 : Function
* Function( ) : always follow "()"
    > https://docs.python.org/3/library/functions.html

* Customize Function( )
    ```=python
    # defining function
    def my_function_name():
        print("hello")
        print("bye")
    ```
    
* While Loop
    ```=python
    While sth_is_true:
        do this
    ```

## Day 7
> -   [Google for Education](https://developers.google.com/edu)-   [Python](https://developers.google.com/edu/python)
>https://developers.google.com/edu/python/lists#for-and-in
>https://developers.google.com/edu/python/lists#range
>https://www.askpython.com/python/python-import-statement

## Day 8 : Argument

* Functions with Inputs
    ```=python
    # defining function
    def my_function_name(something):
        # Do This With Something
        print("hello something")
        print("bye something")
    
    my_function(123)
    # something (parameter 傳入的變數)=123 (argument 傳入的data)
    ```

* Position argument (位置不能變)
    ```=python
    # defining function
    def my_function(a,b,c):
        Do This With a
        Do This With b
        Do This With c

    my_function(1,2,3)
    # a=1
    # b=2
    # c=3
    
    my_function(3,1,2)
    # a=3
    # b=1
    # c=2
    ```
* Keyword argument (位置能變)
    ```=python
    # defining function
    def my_function(a,b,c):
        Do This With a
        Do This With b
        Do This With c

    my_function(a=1,b=2,c=3)
    my_function(c=3,b=2,a=1)
    ```
 * Prime Number
     * 只能被自己跟1整除->不能被分解成更小的數

    
## Day 9 : Dictionaries
* Dictionaries : 
    ```
    {
        Key1:Value,
        Key2:[list], # nesting
        Key3:{dict},
    }
    ```


## Day 10 : Docstrings

![](https://i.imgur.com/1wqAKAc.png)


## Day 12 : Scope

* Scope
    * Local Scope
    * Global Scope

    ```=python
    enemies = "skeleton"

    enemies_num=0

    def increase_enemies():

        # it a totally new viable (create a new viable)

        enemies = "zombie"

        # if try to modify global viable in here
        # need to bring global into local first

        global enemies_num

        enemies_num+=1

    increase_enemies()

    print(f"enemies inside function: {enemies}")
    ```

* Dont try to modify global viable

    ```=python
    # instead

    def increase_enemies():

        print(f"enemies inside function: {enemies}")

        return enemies_num+1

    increase_enemies()

    print(f"enemies outside function: {enemies}")

    ```

* Local Scope
```=PYTHON
def drink_potion():

    potion_strength = 2

    print(potion_strength)

drink_potion_()

# can't find potion_strength -> NameError

print(potion_strength)

```

* Global Scope
    ```
    player_health=10

    def game():

     def drink_potion():
         print(potion_strength)
         print(player_health)

        # need to call drink_potion() here
        drink_potion()

    # HERE cant find drink_potion()
    drink_potion()
    ```
* There is no Block(if/for/while) Scope
    ```=python
    game=3
    enemise=["skeleton","Zombie"]

    if game<5:
        new=enemise[0]

    # still can use viable in block
    print(new)
    ```

* Global Constants (常數) never change->大寫
    ```=python  
    PI = 3.14159
    TWITTER_HANDLE="christine"
    ```

## Day 16 : Class
* Procedural Programming
* Objrct Oriented Programming
    * Class ( ex : Waiter )
        
        * 創造object的blueprint
        * 字首為大寫 
            ```=python
               car   =  Carblueprint()
             (object)     (blueprint)

             從class creat a new object
             ```
        
        * object ( Waiter : marry )
            * attributes (has) : 變量
                * car.speed (car的屬性speed) 
                * `is_holding_plate=true`
            * methods (does) : function
                * car.stop() (car的方法stop())
                * `def take order():`
                 
        * object ( Waiter : john )
            * attributes (has)
            * methods (does) 

## Day 17 : Class

```=python
# Create Class
class User:
    pass

# Create object from class
user_1 = User()
```


* 命名
    * PascalCase (自首大寫) -> ex: class name
    * camelCase
    * snake_case

    >https://www.jetbrains.com/help/pycharm/running-and-debugging-shortcuts.html?keymap=secondary_windows

## Day 19

Function as input

```=pyhton
def function A ():
    PASS
    
# 將function當作參數傳入
def function B (function A):
    PASS
```

* Object instance and state

## Day 21 : Class Inheritance


* class inheritance

```=python
class Animal:

    def __init__(self):

        self.num_eyes = 2
  
    def breathe(self):

        print("Inhale, exhale.")

 
# 繼承class Animal
class Fish(Animal):

    def __init__(self):
        
        # 初始化super class(Animal)繼承Animal的所有屬型和方法
        super().__init__()

```

## Day 26 : Comprehension

* List Comprehension
    ```=python
    new_list = [new_item for item in list]
    ```

* Python Sequence
    > 有一個特定的順序 
    * list
    * range
    * string
    * tuple
    
* Conditional List Comprehension
    ```=python
    new_list = [new_item for item in list if test]
    ```

* Dictionary Comprehension
    ```=python
    new_dict = {new_key:new_value for item in list}

    new_dict = {new_key:new_value for (key,value) in dict.items()

    new_dict = {new_key:new_value for (key,value) in dict.items() if test}
    ```

## Day 27 : Arguments
* Advanced Python Argument
* Argument with default values
    ```=python
    # defining function
    def my_function(a=1,b=2,c=3):
        Do This With a
        Do This With b
        Do This With c

    my_function(a=1,b=2,c=3)
    my_function(c=3,b=2,a=1)
    
* Unlimited Arguments
    ```=python
        def add(n1,n2):
            n1+n2
        add(3,5)

        # *代表可以放讓任意數量的參數->回傳為tuple
        def add(*args):
            for n in args:
                print(n)

        add(3,5,7,8)
    ```    
* Unlimited Keywords Arguments
    ```=python


        # **代表可以放讓任意數量的位置參數->回傳為dict

        def calulate(**kwargs):
            print(kwargs)

        calulate(add=3,substract=5)

        # kwargs = {'add':3,'substract':5}

    ```

    ![](https://i.imgur.com/N5e34sp.png)

## Day 30 : Exceptions
* Catching Exceptions
    ```=python
    try:  
         # sth that might cause an exception

    except:
         # do this if there was an exception

    except:

    else:
        # do this if there were non exceptions

    finally:
        # do this no matter what happens

    ```
* Json

    * Write -> `json.dump()`
    * Read -> `json.load()`
    * Update -> `json.update()`

## Day 33 : API

* Application Programming Interface (API)
    * Is a set of commands,functions,protocols and objects
    * programmers can use to create software or interact with an wxternal system 

* API Endpoint (端點)
    * request data時從哪裡要
    * ex: api.coinbase.com (url) -> coinbase 數據的位置
    * 想要獲得加密數據是->要從api.coinbase.com 

* API Request
* API Parameters : give an input

## Day 34 : Type Hints
* Type Hints
    ```=python
    def greeting(name:str)->str:
        return "Hello" + name
    ```

## Day 35 : Environment Variables
* API Key
    > https://apilist.fun
* Environment Variables ->`env`
    > https://en.wikipedia.org/wiki/Environment_variable
    * purpose:
        1. convenience: 通常在部署大型應用時，在main.py內的某些變量可以被設置為環境變數，使我們可以在不接觸(影響)code的情況下就可以修改這些變量
        2. security: 開發軟體時，可能會在某些地方upload code，環境變數允許我們分開儲存 code and key
    * key=value (可以在我們的應用程式或代碼中使用)



* 可以把key當作環境變數儲存

    * export 變數名稱＝變數數值

* 在MAC中使用環境變數
    ```=python
    (base) kao_oak @ KAOs-MAC : 100 days -> export twilio_key=your_twilio_key
    ```
    ```=python
    # 於code中使用
    import os
    
    key = os.environ.get("twilio_key")
    ```
* 在windows的環境使用環境變數
    ```
    C:\Users\Christine Kao\VS Code> set api_key=your_api_key
    ```

    
    ```=python
    # 於code中使用
    import os
    
    key = os.getenv("PATH")
    ```    

## Day 37 : HTTP Requests
* HTTP Requests
    * GET : `requests.get()`
    * POST : `requests.post()`
    * PUT : `requests.put()`
    * DELETE : `requests.delete()`

* Headers: 包含相關訊息的部分
* Body : 訊息主體

## Day 38 : Authentication

* What is Bearer authentication?

    **Bearer authentication** (also known as **token authentication**) is an HTTP authentication scheme that involves security tokens. 
    
    The name “Bearer authentication” basically means “give access to the bearer of this token.” 
    
    The security token or “bearer token” is just a cryptic string. An example of a bearer token would be a string that could look something like this:
    `AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F`
    
    The idea is that whoever has the secret token, has permission to interact with the spreadsheet. 
    
    A client - like your browser or mobile app - would then send this security token in the Authorization header when making requests to Sheety's server.

* Basic Authentication:
    ![](https://i.imgur.com/wjUOQIY.png)
    
    ```=python
    sheety_response = requests.get(SHEETY_ENDPOINT,auth=HTTPBasicAuth('christine', 'feoijdkslkfskld'))
    ```
    
* Bearer Authentication:
    ```=python
    headers = {"Authorization": "Basic Y2hyaXN0aW5lOmZlb2lqZGtzbGtmc2tsZA=="}
    print(requests.post(endpoint, data=data, headers=headers).json())

    ```
    
## Day 41 : Web

* How do internet work?
    ![](https://i.imgur.com/YGH72CH.png)

* How do websites work?
    ![](https://i.imgur.com/HXAzRDl.png)
    ![](https://i.imgur.com/R0CBzY9.png)


* 從服務器接收的數據通常由三種類型組成(Code Files)
    * If web is a house 
    * HTML:負責網站結構(EX:Button,text/EX:建牆壁，廁所)
    * CSS:負責網站的風格(EX:Button要是紅色的,text是白色的/EX:油漆工，裝修工)
    * JS : 負責網站實際做的事，開始有行為


> [https://codepen.io/pen/?editors=1000](https://codepen.io/)
> https://www.gutenberg.org/ebooks/1661
> https://devdocs.io/

* Introduction to HTML
    * HTML : Hyper Text **Markup** Language
    * XML : Extensible **Markup** Language
    * GML : Generalised **Markup** Language
    * 瀏覽器的目的:解釋Code Files
    * 為網站的基礎架構

* The Anatomy of an HTML Tag
    ![](https://i.imgur.com/3NjefYb.png) 
    * Tag向瀏覽器發出請求，已想要的架構展示

    ![](https://i.imgur.com/EnOcFJ4.png)

    ![](https://i.imgur.com/8V3XOUy.png)
    * Attribute給予瀏覽器更多信息，已指定對該HTML修改

* HTML Boilerplate
    * code template
    ```=html
    # declare doctype(文檔類型) and 
    # 告訴瀏覽器文件打開時使用的HTML版本是甚麼，在此使用的是HTML 5
    <!DOCTYPE html>
    
    # html tag : 告訴瀏覽器，在此區間為html code
    <html lang="en" dir="ltr">
    
      # head tag : 告訴瀏覽器該如何處理該網頁
      <head>
          
        # meta 元素為你的HTML文檔提供額外的數據  
        <meta charset="utf-8">
        
        # title tag
        <title> My Place </title>
      </head>
      
      <body>
          # 標題
          <h1> Christine </h1>
          <p><i> Data Science and Biologist </i> </p>
      </body>
    </html>
    ```

**HTML Tags**

HTML tags contain three main parts: opening tag, content and closing tag. But some HTML tags are unclosed tags.

When a web browser reads an HTML document, browser reads it from top to bottom and left to right. HTML tags are used to create HTML documents and render their properties. Each HTML tags have different properties.

### **Syntax**

```basic
<tag> content </tag>
```

### **HTML Tag Examples**

HTML Tags are always written in lowercase letters. The basic HTML tags are given below:

```basic
<p> Paragraph Tag </p>
<h2> Heading Tag </h2>
<b> Bold Tag </b> 

<i> Italic Tag </i>

<u> Underline Tag</u>
```

###  **Unclosed HTML Tags**

Some HTML tags are not closed, for example br and hr.

```basic
This is code<br>
<hr>
```

**<br> Tag:** br stands for break line, it breaks the line of the code.  
**<hr> Tag:** hr stands for Horizontal Rule. This tag is used to put a line across the webpage.

### **HTML Meta Tags**

DOCTYPE, title, link, meta and style

### **HTML Text Tags**

```basic
<p>  # 段落
<h1>, <h2>, <h3>, <h4>, <h5>, <h6>
<strong>  # 粗體+強調重要性 
<em>  # 斜體+強調 (emphasis)
<i>   # 斜體tag
<b>   # b 粗體 (bold)
<abbr>
<acronym>
<address>
<bdo>
<blockquote>
<cite>
<q>
<code>
<ins>
<del>
<dfn>
<kbd>
<pre>
<samp>
<var> 
<br>
```

### **HTML Link Tags**

```basic
<a>
<base>
```
#anchor tag
![](https://i.imgur.com/15v1zAO.jpg)

### **HTML Image and Object Tags**
![](https://i.imgur.com/PVGRrBS.png)
```basic
<img>
<area>
<map>
<param>
<object>
```

### **HTML List Tags**

```basic
<ul> -- </ul> # An unordered list
<ol> -- </ol> # An ordered list
<li> -- </li> # new list item
<dl> -- </dl>
<dt> -- </dt>
<dd> -- </dd>
```

### **HTML Table Tags**

```basic
<table> -- </table>
<tr> -- </tr>
<td> -- </td>
<th> -- </th>
<tbody> -- </tbody>
<thead> -- </thead>
tfoot
col
olgroup
caption
```

### **HTML Form Tags**

```basic
form
input
textarea
select
option
optgroup
button
label
fieldset
legend
```

### **HTML Scripting Tags**

```basic
script 
noscript
```

## Day 42 : Web
* Cascading Style Sheets (CSS)
    跟 HTML 一樣，CSS 既非標準程式語言，也不是標記語言, 而是一種風格頁面語言（style sheet language）：它能讓你在 HTML 文件中的元素（element）上套用不同的頁面樣式（style）。例如, 當想要將 HTML 頁面上所有段落元素（paragraph elements）裡的文字全部轉換成紅色，你會在CSS裡寫
    ```=html
    p {
      color: red;
    }
    ```
    

```=html

<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title> Kao_oaK'S Site </title>
    
    
  # external CSS
  # 瀏覽器讀到這的時候，會知道網頁的樣式表在這
  # 此時靜態網頁還沒被託管時，不可用跟目錄
  # 此時這個文件在一個較css的文件夾中，並且css的文件夾與index在同一層級
  # 沒有"/"--->這個連接相對於index.html所在的子目錄
  # 我們在person site裡找一個叫css/style.css的文件
  <link rel="stylesheet" href="css/style.css">
  
  # "/"--->使這個連接相對於root，我們正在尋找網站的根源
  <link rel="stylesheet" href="/css/style.css">

  
  # Internal css
  <style media="screen">
    # 選擇要影響的HTML元素 
    body {
      background-color: #EAF6F6; # 改背景顏色
    }

    hr {
      border-style: none;  # 更改瀏覽器的預設值
      
      border-style: dotted none none; # 第一個影響top，第二個影響left/right，第三個影響bottom(三個值得時候)
      or
      border-top-style: dotted;
      
      border-color: grey;
      border-width: 10px;
      width: 30%;

    }

    img {
      height: 100px;   # 圖片的框框現在只有100像素高
    }
    
  </style>
</head>



# style takes css code , use ';' to close css code
<body style="background-color:#EAF6F6;">
  <table cellspacing="20">
    <td>
      # if 瀏覽器不能渲染圖象，會簡單的顯示描述文字來替代圖像 <br>
      # 瀏覽器會試圖ping圖片的server，試圖獲得這張圖片
      <br>
      <img src="images/circle-cropped.png" alt="my profile's picture">
      
      
      # src(source)/alt(tag)為HTLM Attribute
      # class="bacon" 為新增加的class Attribute，允許我們區分所有不同的HTML元素
      <img class="bacon" src="https://emojipedia-us.s3.amazonaws.com/thumbs/240/apple/118/bacon_1f953.png" alt="bacon-img">
      
      
      
    </td>
    <td>
      # h1 標題
      <h1> Christine </h1>

      # p 段落
      <p> <em> <strong> Data Science and <a href="https://en.wikipedia.org/wiki/Biologist">Biologist</a></strong> </em> </p>
      <p> I'm a new to scientist and learn machine learning </p>
    </td>
  </table>


  # hr 分隔線
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">
  <h3> Education </h3>
  # ul 未排序list
  <ul>
    <li> colledue </li>
    <li> master degree </li>
  </ul>

  <hr style="height:2px;border-width:0;color:gray;background-color:gray">
  <h3> my hobbit </h3>
  # ol 排序list
  <ol>
    <li> jump </li>
    <li> run </li>
  </ol>

  <hr style="height:2px;border-width:0;color:gray;background-color:gray">
  <h3> Work Experience </h3>
  # 表格
  <table cellspacing="10">

    # table head
    <thead>
      <tr>
        # table header cell
        <th> Dates </th>
        <th> Works </th>
      </tr>
    </thead>

    # table body
    <tbody>

    </tbody>

    # table foot
    <tfoot>

    </tfoot>

    # tr : table row
    <tr>
      # td : table cell
      <td>2010-2012</td>
      <td>fju</td>
    </tr>

    <tr>
      <td>2014-2016</td>
      <td>cgu</td>
    </tr>
  </table>

  <hr style="height:2px;border-width:0;color:gray;background-color:gray">
  <h3> My Skills </h3>
  <table cellspacing="10">
    <tr>
      <td> Python </td>
      <td> 🌟🌟🌟🌟 </td>
      <td> R </td>
      <td> 🌟🌟 </td>
    </tr>
    <tr>
      <td> AWS </td>
      <td> 🌟🌟🌟 </td>
      <td> GCP </td>
      <td> 🌟🌟🌟 </td>
    </tr>
  </table>

  <hr style="height:2px;border-width:0;color:gray;background-color:gray">
  # 內部超連結 <br>
  <a href="contacts.html"> My Contacts </a>
</body>

</html>

```

### Debug
![](https://i.imgur.com/zLOrBiy.png)

可以看到有三個顏色要套用到body，重要順序如下
1. HTML element : white被應用在實際body元素的樣式屬性上
1. internal CSS : red來自index.html的第9行
    > 在單個頁面上，可以通過使用element或是internal CSS來應用更具體的規定，作為特定頁面的變化改變
3. CSS規則 : #EAF6F6套用了style.css文件中的CSS規則
    > 全局性CSS規則可以應用到所有的網頁    

### CSS Syntax (The Grammar of the CSS Languaue)

讓我們深入解析下列的 CSS：
    ![](https://i.imgur.com/W2aVbGW.png)
    
```=html
selector {bproperty:value;}
```

* 選擇器（Selector）
    在這個規則的最前頭為 HTML 的元素名。它將決定你 HTML 裡什麼元素將被你接下來的設定影響（在這個範例中,就是 段落元素 p）。若要改變欲影響的元素，只要更改選擇器就行了。
    
* 宣告（Declaration）
    單一個規則，例如 color: red; 指定了這個元素的呈現樣貌。
    
* 屬性 (Properties)
    修改屬性是改變你HTML元素的一種方法 . (在這範例中, color 是段落（p）元素的一種屬性.) 在CSS中, 你可以選擇哪些屬性用來影響 rule.
    
* 屬性值 (Property value)
    屬性值 就是位於屬性右邊，在冒號（:）之後，從眾多的可能樣式選出一個給予屬性（範例中就是從眾多的 color 樣式中選出 red）
    
* 注意語法其他重要的部分：
    * 每一個規則當中，除了選擇器名稱以外，其他都必須被大括號（{}）給包住.
    * 在每一個宣告裡面，屬性跟屬性值之間必須用冒號(:) 做區分。
    * 在每一個規則裡面可以包含有許多宣告，但不同的宣告之間必須使用分號 (;) 來區分。

## Day 43 : CSS
* The CSS bOX Model
![](https://i.imgur.com/MhXbCNB.png)
![](https://i.imgur.com/aaR5u7u.png)

此時box1總寬度為260
![](https://i.imgur.com/tc1tftd.png)

若要移動第二個box到對角
可以設 margin-left: 260px;
![](https://i.imgur.com/tWnMtDi.png)

* CSS Display property
    * Block Element - 佔據網頁上整個螢幕的寬度，進而阻擋其他元素座落在其左邊或右邊 
        *  Paragraphs(\<p>)
        *  Headers(\<h1> through \<h6>)
        *  Divisions(\<div>)
        *  Lists and list items(\<ol>, \<ul> and \<li>)
        *  Forms(\<form>)
        
    * Inline Element(内坎式) - 在高度和寬度上只佔用所需的空間(無法改變元素寬度)
        * Spans(\<span>)
        * Images(\<img>)
        * Anchors(\<a>) 
        
    * Inline-block Element - 既可以放在同一行上又可以改變寬度
    
    * None Element - 將其顯示值設為無，元素不會顯示出來，可以用來隱藏網頁上的東西
        * 或是使用property - visibility(隱藏但原來的位置仍被保留)

            ```=CSS
            P{
             background-color:blue;
             display:inline-block;
             visibility:hidden;
            }
            ```
            
* CSS Positioning
    * 即使沒有CSS，HTML元素已有預設的規則
        1. Content is Everything : 內容首先決定了多大，多寬，多高。
        2. Order Comes From Code : 屏幕上HTML元素的順序來自於HTML Code。
        3. Children Sit On Parents
            ```=CSS
            <div>
                <h1>a <span>pro<\span> grammer<\h1>
            </div>
            ```
            我們首先有div,然後h1，span，從下到上的層級制度

    * CSS Position Property
        * Static : 照原本的HTML規則，保持預設的規定
        * Relative : 將我們選擇的元素相對於它本來顯示的位置進行定位，不影響螢幕上任何其他元素的布局(原本空的還卡在原位置，所以其他不會跟著移動)
            > 相對定位代表要adding a margin relative to where the element should been
            ```=CSS
            img{
            position:relative
            left:30px;
            }
            # 圖片(左側)從前一個的位置(左側)移動30px
            ```
            * Coordinates 座標屬性
                * Top
                * Bottom
                * Left
                * Right
        
        
        * Absolute
            影響螢幕上任何其他元素的布局
            > 絕對定位代表要adding a margin to its parent element
            ```=CSS
            # img nest in div
            div{
                position:relative
            }
            
            img{
                position:absolute
                right:30px
            }
            
            # 現在圖片元素和父元素(div)之間增加了30px的右邊距)
            ```
        * Fixed
            滾動網頁時， 被fixed的物件就會停留在當前位置
            
    * Font Family
        * sans-serif
        
        * serif
        * monospace
