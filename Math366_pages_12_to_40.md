

<!-- PAGE_START_12 -->
### صفحة 12

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>1-1 مشتقة تركيب دالتين</h2>
<p><strong>Derivative of Composite Functions</strong></p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
تعلم أن تركيب دالتين هي طريقة أخرى تستعمل لدمج الدوال، فمثلاً إذا كانت $y = f_1(z), z = f_2(x)$ ، فإنه يمكن التعبير عن الدالة $y$ بدلالة المتغير $x$ ، وتسمى دالة الدالة (الدالة المركبة)، وتكتب على الصورة $y = f_1[f_2(x)]$.
<br>
ويرمز لها بالرمز $[f_1 \circ f_2](x)$ وتُقرأ $f_1$ بعد $f_2$ ، أو $f_1 \text{ circle } f_2(x)$ .
<br>
وعلى سبيل المثال، إذا كانت $f_1(x) = 3x + 4 , f_2(x) = 6x$ ، فإن:
</div>

$$[f_1 \circ f_2](x) = f_1[f_2(x)]$$
$$= f_1(6x) = 3(6x) + 4$$
$$= 18x + 4$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وهي الدالة الناتجة عن تركيب $f_1 , f_2$ ، ولكن ليست جميع الدوال قابلة للتركيب، حيث أنه لتركيب دالتين شرط نقدمه فيما يأتي:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>شرط تركيب دالتين</strong>
<br>
<strong>مفهوم أساسي:</strong>
<br>
<strong>التعبير اللفظي:</strong> إذا كانت $f_1, f_2$ دالتين، فإن التركيب $[f_1 \circ f_2]$ يُمثل دالة، إذا كان مدى $f_2$ مجموعة جزئية من مجال $f_1$.
<br>
<strong>بالرموز:</strong> $\text{مجال } f_1 \supseteq \text{مدى } f_2$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1:</strong>
إذا كانت $f_1(x) = |x|, f_2(x) = x + 1$ ، فهل $[f_2 \circ f_1](x)$ يُمثل دالة؟
<br><br>
<strong>الحل:</strong>
</div>

$$\because f_1(x) = |x|$$

$$\therefore \text{مدى } f_1(x) \text{ هو } [0, \infty)$$

$$\because f_2(x) = x + 1$$

$$\therefore \text{مجال } f_2(x) \text{ هو } \mathbb{R}$$

$$\because \text{مجال } f_2(x) \supset \text{مدى } f_1(x)$$

$$\therefore [f_2 \circ f_1](x) \text{ يُمثل دالة.}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 1 الاشتقاق | 12
</div>
<!-- PAGE_END_12 -->


<!-- PAGE_START_13 -->
### صفحة 13

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2):</strong><br>
إذا كانت $f(x) = x^2 - 1 \quad , \quad g(x) = \sqrt{x}$ ، فأي مما يأتي يُمثّل دالة؟
$$[f \circ g](x) \quad , \quad [g \circ f](x)$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
مدى $g(x)$ هو $[0, \infty)$ ، مجال $f(x)$ هو $\mathbb{R}$<br>
$\because$ مدى $g(x) \subseteq$ مجال $f(x)$<br>
$\therefore [f \circ g](x)$ يُمثّل دالة<br>
مدى $f(x)$ هو $[-1, \infty)$ ، مجال $g(x)$ هو $[0, \infty)$<br>
$\because$ مدى $f(x) \not\subseteq$ مجال $g(x)$<br>
$\therefore [g \circ f](x)$ لا يُمثّل دالة
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (3):</strong><br>
إذا كانت $Z = 6x + 5 \quad , \quad y = 12 Z^{-\frac{2}{3}} - 1$ ، فهل يمكن إيجاد $\frac{dy}{dx}$ ؟
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
$$\because y = 12 Z^{-\frac{2}{3}} - 1 \quad , \quad Z = 6x + 5$$
$$\therefore y = 12(6x + 5)^{-\frac{2}{3}} - 1$$
وهي تركيب الدالة $y$ مع الدالة $Z$<br>
ووفقاً لما سبقت دراسته في قواعد الاشتقاق، فإنه لا يمكن إيجاد $\frac{dy}{dx}$.<br>
لذا سنقدم نظرية مشتقة الدالة المركبة (دالة الدالة) التي تيسر لنا عملية اشتقاق مثل هذه الدوال.
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9;">
<strong>مشتقة دالة الدالة (الدالة المركبة)</strong><br><br>
<strong>نظرية:</strong><br>
إذا كانت $y = f_1(z)$ قابلة للاشتقاق بالنسبة إلى $z$ ، و $z = f_2(x)$ قابلة للاشتقاق بالنسبة إلى $x$ ، فإن الدالة المركبة $y = [f_1 \circ f_2](x)$ تكون قابلة للاشتقاق بالنسبة إلى $x$ ويكون:
$$\frac{dy}{dx} = \frac{dy}{dz} \cdot \frac{dz}{dx}$$
وتسمى هذه المشتقة بقاعدة التسلسل (The Chain Rule) ، وبتعبير آخر:
$$[f_1 \circ f_2]'(x) = f_1'[f_2(x)] \cdot f_2'(x)$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 1-1 مشتقة تركيب دالتين 13
</div>
<!-- PAGE_END_13 -->


<!-- PAGE_START_14 -->
### صفحة 14

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>البرهان</b>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذا كانت $\Delta x$ مقدار التغيّر في $x$، $\Delta y$ مقدار التغيّر في $y$، $\Delta z$ مقدار التغيّر في $z$، فإن:
</div>

$$ \frac{\Delta y}{\Delta x} = \left(\frac{\Delta y}{\Delta x}\right)\left(\frac{\Delta z}{\Delta z}\right) $$
$$ = \left(\frac{\Delta y}{\Delta z}\right)\left(\frac{\Delta z}{\Delta x}\right) $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبإيجاد النهاية للطرفين عندما تقترب $\Delta x$ من الصفر، فإن:
</div>

$$ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \left( \left(\frac{\Delta y}{\Delta z}\right)\left(\frac{\Delta z}{\Delta x}\right) \right) $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عندما $\Delta x \to 0$، فإن $\Delta z \to 0$، ويكون:
</div>

$$ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \left( \lim_{\Delta z \to 0} \frac{\Delta y}{\Delta z} \right) \left( \lim_{\Delta x \to 0} \frac{\Delta z}{\Delta x} \right) $$

$$ \frac{dy}{dx} = \left(\frac{dy}{dz}\right)\left(\frac{dz}{dx}\right) $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>ملاحظة:</b> جميع الدوال في الأمثلة والتمارين الآتية تحقق شرط التركيب.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 4:</b> إذا كانت $f(x) = 10x + 3 , g(x) = \sqrt[3]{x}$ ، فأوجد $[f \circ g]'(x)$ ، ثم أوجد قيمة $[f \circ g]'(2\sqrt{2})$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
</div>

$$ \because [f \circ g]'(x) = f'[g(x)] g'(x) $$
$$ \therefore [f \circ g]'(x) = (10) \left[ \frac{1}{3 \sqrt[3]{x^2}} \right] $$
$$ [f \circ g]'(2\sqrt{2}) = (10) \left[ \frac{1}{3 \sqrt[3]{(2\sqrt{2})^2}} \right] $$
$$ = \frac{5}{3} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>حل آخر</b>
</div>

$$ \because [f \circ g](x) = f[g(x)] $$
$$ = f(\sqrt[3]{x}) $$
$$ = 10 \sqrt[3]{x} + 3 $$
$$ \therefore [f \circ g]'(x) = (10) \left[ \frac{1}{3 \sqrt[3]{x^2}} \right] $$
$$ [f \circ g]'(2\sqrt{2}) = \frac{10}{3 \sqrt[3]{(2\sqrt{2})^2}} $$
$$ = \frac{5}{3} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 1 الاشتقاق | 14
</div>
<!-- PAGE_END_14 -->


<!-- PAGE_START_15 -->
### صفحة 15

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5</strong>
<br>
إذا كانت $z = y^3 - 2y + 1 \text{ ، } y = x^2$ ، فأوجد $\frac{dz}{dx}$ عند $x = 1$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = x^2$$
$$\frac{dy}{dx} = 2x$$
$$\because z = y^3 - 2y + 1$$
$$\frac{dz}{dy} = 3y^2 - 2$$
$$\frac{dz}{dx} = \left(\frac{dz}{dy}\right) \left(\frac{dy}{dx}\right)$$
$$\frac{dz}{dx} = (3y^2 - 2)(2x) \quad , \quad y = x^2$$
$$= (3x^4 - 2)(2x)$$
$$\left(\frac{dz}{dx}\right)_{x=1} = (3 - 2)2 = 2$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>حل آخر</strong>
</div>

$$y = x^2 \quad , \quad z = y^3 - 2y + 1$$
$$z = (x^2)^3 - 2x^2 + 1$$
$$= x^6 - 2x^2 + 1$$
$$\frac{dz}{dx} = 6x^5 - 4x$$
$$\left(\frac{dz}{dx}\right)_{x=1} = 6 - 4 = 2$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 6</strong>
<br>
إذا كانت $z = y^3 \text{ ، } y = \sqrt{x} - 3$ ، فأوجد $\frac{dz}{dx}$ عندما $x = 25$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = \sqrt{x} - 3$$
$$\frac{dy}{dx} = \frac{1}{2\sqrt{x}}$$
$$\because z = y^3$$
$$\frac{dz}{dy} = 3y^2 = 3\left(\sqrt{x} - 3\right)^2$$
$$\frac{dz}{dx} = \left(\frac{dz}{dy}\right) \left(\frac{dy}{dx}\right)$$
$$= 3\left(\sqrt{x} - 3\right)^2 \left(\frac{1}{2\sqrt{x}}\right)$$

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>15</strong> |الدرس 1-1 مشتقة تركيب دالتين
</div>
<!-- PAGE_END_15 -->


<!-- PAGE_START_16 -->
### صفحة 16

$$\left(\frac{dz}{dx}\right)_{x=25} = \frac{3(\sqrt{25}-3)^2}{2\sqrt{25}}$$
$$= \frac{3(4)}{2(5)}$$
$$= \frac{6}{5}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 1</strong>
<br>
أوجد $\frac{dy}{dx}$ إذا كانت:
<br>
a) $y = \frac{3}{z+1} \ , \ z = 3x^2 - 4$
<br>
b) $y = \sqrt{z} \ , \ z = 1 - 4x^2$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 7</strong>
<br>
إذا كانت $y = z^{10} \ , \ z = x^3 + 1$ ، فأوجد $\frac{dy}{dx}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\frac{dy}{dx} = \left(\frac{dy}{dz}\right)\left(\frac{dz}{dx}\right)$$
$$= (10 z^9) (3 x^2) \quad , \quad z = x^3 + 1$$
$$\frac{dy}{dx} = 10 (x^3 + 1)^9 (3 x^2)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
لاحظ أن:
<br>
$y = z^{10} \quad , \quad z = x^3 + 1$
</div>

$$\frac{dy}{dx} = 10 (x^3 + 1)^9 (3 x^2)$$

$$\frac{dy}{dx} = \left(\frac{dy}{dz}\right)\left(\frac{dz}{dx}\right)$$
$$= (n z^{n-1})\left(\frac{dz}{dx}\right)$$
$$= n (g(x))^{n-1} (g'(x))$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
لاحظ أن: $y = (g(x))^n$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
16 الفصل 1 الاشتقاق
</div>
<!-- PAGE_END_16 -->


<!-- PAGE_START_17 -->
### صفحة 17

<div dir="rtl" style="text-align: right; font-size: 16px;">
وهذا يقودنا إلى النتيجة الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #cce5ff; background-color: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px;">
<strong>نتيجة</strong><br><br>
إذا كانت:
$$y = [f(x)]^n \quad , \quad n \in \mathbb{R}$$
فإن:
$$\frac{dy}{dx} = n[f(x)]^{n-1} (f'(x))$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 8</strong><br>
أوجد $\frac{dy}{dx}$ إذا كانت:
<p>a) $y = (15x^3 - 7x^2 + 2)^9$</p>
<p>b) $y = \sqrt{x^3 - 5}$</p>
<p>c) $y = \frac{1}{(2x^2 - 1)^5}$</p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(a
$$\because y = (15x^3 - 7x^2 + 2)^9$$
$$\therefore \frac{dy}{dx} = 9(15x^3 - 7x^2 + 2)^8 (45x^2 - 14x)$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(b
$$\because y = \sqrt{x^3 - 5}$$
$$\therefore \frac{dy}{dx} = \frac{1}{2} (x^3 - 5)^{-\frac{1}{2}} (3x^2)$$
$$= \frac{3x^2}{2\sqrt{x^3 - 5}}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(c
$$\because y = \frac{1}{(2x^2 - 1)^5}$$
$$\therefore \frac{dy}{dx} = -5(2x^2 - 1)^{-6} (4x)$$
$$= \frac{-20x}{(2x^2 - 1)^6}$$
</div>

<br>
<hr>
<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 1-1 مشتقة تركيب دالتين &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 17
</div>
<!-- PAGE_END_17 -->


<!-- PAGE_START_18 -->
### صفحة 18

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 9:</strong> إذا كانت $y = (2x + 7)^5 (4x - 1)^3$ ، فأوجد $\frac{dy}{dx}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = (2x + 7)^5 (4x - 1)^3$$

$$\therefore \frac{dy}{dx} = (2x + 7)^5 \left( \frac{d}{dx} (4x - 1)^3 \right) + (4x - 1)^3 \left( \frac{d}{dx} (2x + 7)^5 \right)$$

$$= (2x + 7)^5 (3(4x - 1)^2 (4)) + (4x - 1)^3 (5(2x + 7)^4 (2))$$

$$= 12(2x + 7)^5 (4x - 1)^2 + 10(4x - 1)^3 (2x + 7)^4$$

$$= 2(2x + 7)^4 (4x - 1)^2 [6(2x + 7) + 5(4x - 1)]$$

$$= 2(2x + 7)^4 (4x - 1)^2 (32x + 37)$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 10:</strong> إذا كانت $z = y^3$ ، فأوجد $\frac{dy}{dx}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because z = y^3$$

$$\therefore \frac{d}{dx} (z) = \left( \frac{dz}{dy} \right) \left( \frac{dy}{dx} \right)$$

$$\frac{dz}{dx} = (3y^2) \left( \frac{dy}{dx} \right)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فمثلاً:
</div>

$$\frac{d}{dx} (z^5) = 5 z^4 \frac{dz}{dx} \quad , \quad \frac{d}{dx} (u^{-3}) = -3 u^{-4} \frac{du}{dx}$$

$$\frac{d}{dx} (y^7) = 7 y^6 \frac{dy}{dx} \quad , \quad \frac{d}{dx} (x^5) = 5 x^4$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
18 الفصل 1 الاشتقاق
</div>
<!-- PAGE_END_18 -->


<!-- PAGE_START_19 -->
### صفحة 19

<div dir="rtl" style="text-align: right; font-size: 16px;">
وهذا يقودنا إلى النتيجة الآتية:
</div>

> **نتيجة 2**
> 
> <div dir="rtl" style="text-align: right; font-size: 16px;">
> إذا كانت:
> </div>
> 
> $$y = f(x)$$
> 
> <div dir="rtl" style="text-align: right; font-size: 16px;">
> فإن:
> </div>
> 
> $$\frac{d}{dx}(y^n) = n y^{n-1} \frac{dy}{dx} \quad, \quad n \in R^*$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: red;">الاشتقاق الضمني</h3>

الدالة الضمنية هي دالة تظهر على الصورة $f(x, y) = 0$ حيث $f(x, y)$ هي علاقة تربط المتغير $x$ بالمتغير $y$ ، وفي بعض الأحيان يمكن التعبير عن $y$ صراحة بدلالة $x$ ، ولكن في الأغلب يتعذر ذلك. وللحصول على $\frac{dy}{dx}$ نشتق هذه العلاقة بالنسبة إلى المتغير $x$ ، فنحصل على متساوية على الصورة:
</div>

$$f\left(x, y, \frac{dy}{dx}\right) = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويمكننا إيجاد $\frac{dy}{dx}$ باستعمال النتيجة 2 كما سيتضح من الأمثلة الآتية:
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 11:</strong> أوجد $\frac{dy}{dx}$ في كل مما يأتي:
</div>

$$a) \quad x^2 + y^2 = 9$$

$$b) \quad \sqrt{x} + \sqrt{y} = 4$$

$$c) \quad 3x + x^2 y - 5y^2 = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h4 style="color: blue;">الحل</h4>

<strong>a)</strong> $\because x^2 + y^2 = 9$
<br>
وباشتقاق الطرفين بالنسبة للمتغير $x$
</div>

$$\therefore 2x + 2y \left(\frac{dy}{dx}\right) = 0$$

$$\frac{dy}{dx} = \frac{-x}{y}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>b)</strong> $\because \sqrt{x} + \sqrt{y} = 4$
<br>
وباشتقاق الطرفين بالنسبة للمتغير $x$
</div>

$$\therefore \frac{1}{2}x^{-\frac{1}{2}} + \frac{1}{2}y^{-\frac{1}{2}} \frac{dy}{dx} = 0$$

$$\frac{dy}{dx} = -\sqrt{\frac{y}{x}}$$

---
<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 1-1 مشتقة تركيب دالتين | 19
</div>
<!-- PAGE_END_19 -->


<!-- PAGE_START_20 -->
### صفحة 20

<div dir="rtl" style="text-align: right; font-size: 16px;">
$$\because 3x + x^2 y - 5y^2 = 0 \quad \text{(c}$$

وباشتقاق الطرفين بالنسبة للمتغير $x$

$$\therefore 3 + x^2 \frac{dy}{dx} + y(2x) - 5(2y) \frac{dy}{dx} = 0$$
$$\frac{dy}{dx}(x^2 - 10y) = -2xy - 3$$
$$\frac{dy}{dx} = \frac{-2xy - 3}{x^2 - 10y}$$
$$= \frac{2xy + 3}{10y - x^2}$$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 12</strong>

إذا كان $4x^2 + xy - 3y^2 = 0$ ، فأوجد $\frac{dy}{dx}$ عند النقطة $(-2, 2)$ .

<br>

<strong>الحل</strong>

$$\because 4x^2 + xy - 3y^2 = 0$$

وباشتقاق الطرفين بالنسبة للمتغير $x$

$$\therefore 8x + x \frac{dy}{dx} + y - 3(2y) \frac{dy}{dx} = 0$$
$$\frac{dy}{dx} (x - 6y) = -8x - y$$
$$\frac{dy}{dx} = \frac{-8x - y}{x - 6y}$$
$$\left(\frac{dy}{dx}\right)_{(-2, 2)} = \frac{-8(-2) - 2}{-2 - 6(2)}$$
$$= \frac{14}{-14}$$
$$= -1$$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 2</strong>

أوجد $\frac{dy}{dx}$ في كلٍّ مما يأتي:

a) $y^2 + 3xy = 10$ عند النقطة $(1, 2)$ .

b) $4x^2 + 9y^2 = 40$ عند النقطة $(1, 2)$ .

c) $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ، حيث كل من $a, b$ عدد حقيقي

d) $x^2 - 2xy + y^2 = 16$ عند النقطة $(-1, 3)$
</div>
<!-- PAGE_END_20 -->


<!-- PAGE_START_21 -->
### صفحة 21

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 13</strong>
<br>
إذا كانت $g'(x) = \sqrt{3x + 7}$ ، $f(x) = x^2 + 5x$، فأوجد $[g \circ f]'(1)$.
<br><br>
<strong>الحل</strong>
</div>

$$ \because f(x) = x^2 + 5x, \quad g'(x) = \sqrt{3x + 7} $$

$$ \therefore [g \circ f]'(x) = g'(f(x)) f'(x) $$

$$ = \left( \sqrt{3(x^2 + 5x) + 7} \right) (2x + 5) $$

$$ [g \circ f]'(1) = \left( \sqrt{3(1 + 5(1)) + 7} \right) (2(1) + 5) $$

$$ = 35 $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 14</strong>
<br>
إذا كانت $h(x) = 3x$ ، $g'(x) = \sec^2 x$، فأوجد $[g \circ h]'\left(\frac{\pi}{3}\right)$.
<br><br>
<strong>الحل</strong>
</div>

$$ \because [g \circ h]'(x) = g'[h(x)] h'(x) $$

$$ = \sec^2 3x(3) $$

$$ = 3 \sec^2 3x $$

$$ \therefore [g \circ h]'\left(\frac{\pi}{3}\right) = 3 \sec^2 3\left(\frac{\pi}{3}\right) $$

$$ = 3 \sec^2 \pi $$

$$ = 3(-1)^2 $$

$$ = 3 $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 1-1 مشتقة تركيب دالتين 21
</div>
<!-- PAGE_END_21 -->


<!-- PAGE_START_22 -->
### صفحة 22

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين 1-1</h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
1. إذا كانت $f(x) = x + 3$ ، $g(x) = 2x^3$ ، فأوجد $[f \circ g]'(x)$ عند $x = 1$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2. إذا كانت $f(x) = \sqrt[3]{x}$ ، $g(x) = x^3$ ، فأوجد $[f \circ g]'(x)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3. إذا كانت $h(x) = 2x$ ، $g'(x) = \sin x$ ، فأوجد $[g \circ h]'\left(\frac{\pi}{6}\right)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
4. أوجد $\frac{dy}{dx}$ في كل مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $y = (7 + 3x)^5$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
b) $y = (x^3 + 3x^2 + 2)^7$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
c) $y = \frac{1}{(x^3 - 3x^2)^3} \quad , \quad x = 1$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
d) $y = z^5 \quad , \quad z = x^2 + 7 \quad , \quad x = 2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
e) $y = (x - 1)^4 (x + 1)^6$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
f) $y = \frac{-1}{z} \quad , \quad z = x^3 + x^2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
g) $y = \left(\frac{x}{x + 1}\right)^8$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
5. إذا كانت $y = (1 - 2x + x^2)^8$ ، فأثبت أن $\frac{dy}{dx}(1 - x) + 16y = 0$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
6. إذا كان $(x^2 - a)^2 = 4y$ ، حيث $a$ عدد حقيقي، فأثبت أن $\left(\frac{dy}{dx}\right)^2 - 4x^2 y = 0$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
7. إذا كانت $z = x^3 - 1$ ، $y = z^2 - 7z + 3$ ، فأثبت أن $\frac{dy}{dx} + 9\frac{dz}{dx} - 6x^5 = 0$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
8. إذا كانت $y = (3x^2 - 2)^3 (5x - 7)$ ، فأوجد $\frac{dy}{dx}$ عند النقطة $(1, -2)$.
</div>
<!-- PAGE_END_22 -->


<!-- PAGE_START_23 -->
### صفحة 23

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>9</b> إذا كانت $y = \sqrt[3]{(x^2 - 3x - 4)^2}$ ، فأوجد $\frac{dy}{dx}$ .
</div>

<p></p>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>10</b> أوجد $\frac{d}{dx} \left( \sqrt[3]{x^2 + 4} \right)$ عند $x = \sqrt{5}$ .
</div>

<p></p>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>11</b> أوجد $\frac{dy}{dx}$ في كل مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-right: 20px;">
a) $\frac{1}{x} + \frac{1}{y} = 2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-right: 20px;">
b) $\frac{x}{y} - 4y = x$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-right: 20px;">
c) $\sqrt{xy^2 + yx^2} = 1$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-right: 20px;">
d) $y + \sqrt{xy} = 3x^2$
</div>

<p></p>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>12</b> إذا كان $x^2 + 2y^2 + 4x - 12y + 11 = 0$ ، فأوجد النقاط التي تكون عندها $\frac{dy}{dx} = -\frac{3}{2}$ .
</div>

<p></p>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>13</b> إذا كان $y^3 + 2x^2 y - 3xy^2 = 0$ ، فأوجد $\frac{dy}{dx}$ عند النقطة $(1, 1)$ .
</div>

<p></p>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>14</b> إذا كان $y^2 - 3x^2 + 2x = 0$ ، فأثبت أن $y^2 \left( \frac{dy}{dx} \right)^2 - (3x - 1)^2 = 0$ .
</div>

<p></p>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>15</b> إذا كان $y^2 = ax^2 - a^2$ ، حيث $a$ عدد حقيقي، فأثبت أن
$$\frac{y^2}{x^2} \left( \frac{dy}{dx} \right)^2 - xy \left( \frac{dy}{dx} \right) + y^2 = 0$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 1-1 مشتقة تركيب دالتين &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>23</b>
</div>
<!-- PAGE_END_23 -->


<!-- PAGE_START_24 -->
### صفحة 24

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>1-2 مشتقات الدوال المثلثية</h2>
<h3>Derivatives of Trigonometric Functions</h3>

<p>في هذا الدرس سوف تدرس اشتقاق الدوال المثلثية مثل:</p>
</div>

$$y = \sin x, \quad y = \cos x, \quad y = \tan x$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p>وهذه الدراسة تحتاج إلى النظرية الآتية:</p>
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نظرية</strong>
</div>

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1</strong>
<p>أوجد كلّاً مما يأتي:</p>
<p><strong>a)</strong> $\lim_{x \to 0} \frac{\sin 5x}{x}$</p>
<p><strong>b)</strong> $\lim_{x \to 0} \frac{x + \sin 2x}{x}$</p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
<p><strong>a)</strong></p>
</div>

$$\lim_{x \to 0} \frac{\sin 5x}{x} = \lim_{5x \to 0} \frac{5 \sin 5x}{5x}$$
$$= \left( \lim_{5x \to 0} 5 \right) \left( \lim_{5x \to 0} \frac{\sin 5x}{5x} \right)$$
$$= (5) (1) \quad \text{لماذا؟}$$
$$= 5$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p><strong>b)</strong></p>
</div>

$$\lim_{x \to 0} \frac{x + \sin 2x}{x} = \lim_{x \to 0} \left( \frac{x}{x} + \frac{\sin 2x}{x} \right)$$
$$= \lim_{2x \to 0} \left( 1 + \frac{2 \sin 2x}{2x} \right)$$
$$= \lim_{2x \to 0} 1 + 2 \lim_{2x \to 0} \frac{\sin 2x}{2x}$$
$$= 1 + 2(1)$$
$$= 3$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الفصل 1</strong> الاشتقاق | <strong>24</strong>
</div>
<!-- PAGE_END_24 -->


<!-- PAGE_START_25 -->
### صفحة 25

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة</strong>
</div>

$$\lim_{x \to 0} \frac{\tan x}{x} = 1$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان</strong>
</div>

$$\lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \left[ \left( \frac{\sin x}{\cos x} \right) \left( \frac{1}{x} \right) \right]$$
$$= \left( \lim_{x \to 0} \frac{\sin x}{x} \right) \left( \lim_{x \to 0} \frac{1}{\cos x} \right)$$
$$= 1 \quad \text{لماذا؟}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 2</strong>: أوجد $\lim_{x \to 0} \frac{\tan 3x}{x}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\lim_{x \to 0} \frac{\tan 3x}{x} = \left( \lim_{3x \to 0} 3 \right) \left( \lim_{3x \to 0} \frac{\tan 3x}{3x} \right)$$
$$= (3)(1) = 3$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نظرية</strong>
</div>

$$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3</strong>: أثبت أن $\lim_{x \to 0} \frac{2x + 1 - \cos x}{3x} = \frac{2}{3}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\text{L.H.S} = \lim_{x \to 0} \frac{2x + 1 - \cos x}{3x}$$
$$= \lim_{x \to 0} \left( \frac{2x}{3x} + \frac{1 - \cos x}{3x} \right)$$
$$= \lim_{x \to 0} \left( \frac{2x}{3x} \right) + \lim_{x \to 0} \left( \frac{1 - \cos x}{3x} \right)$$
$$= \lim_{x \to 0} \left( \frac{2}{3} \right) + \frac{1}{3} \lim_{x \to 0} \left( \frac{1 - \cos x}{x} \right)$$
$$= \left( \frac{2}{3} \right) + \left( \frac{1}{3} \right) (0) \quad \text{لماذا؟}$$
$$= \frac{2}{3} + 0$$
$$= \frac{2}{3}$$
$$= \text{R.H.S}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
25 | الدرس 2-1 مشتقات الدوال المثلثية
</div>
<!-- PAGE_END_25 -->


<!-- PAGE_START_26 -->
### صفحة 26

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نظرية</strong>
<br>
إذا كانت:
</div>

$$f(x) = \sin x$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فإن:
</div>

$$f'(x) = \cos x$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان</strong>
<br><br>
باستعمال تعريف المشتقة:
</div>

$$\therefore f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

$$\therefore f'(x) = \lim_{h \to 0} \frac{\sin (x+h) - \sin x}{h}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
باستعمال قانون جيب مجموع زاويتين:
</div>

$$f'(x) = \lim_{h \to 0} \left[ \frac{\sin x \cos h + \cos x \sin h - \sin x}{h} \right]$$

$$= \lim_{h \to 0} \left[ \sin x \left( \frac{\cos h - 1}{h} \right) + \cos x \left( \frac{\sin h}{h} \right) \right]$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
باستعمال النظريتين السابقتين نحصل على:
</div>

$$f'(x) = \sin x (0) + \cos x (1)$$

$$\therefore f'(x) = \cos x$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>2 نتيجة</strong>
<br>
إذا كانت:
</div>

$$f(x) = \sin (g(x))$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فإن:
</div>

$$f'(x) = \cos (g(x)) \cdot (g'(x))$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>26</strong> الفصل 1 الاشتقاق
</div>
<!-- PAGE_END_26 -->


<!-- PAGE_START_27 -->
### صفحة 27

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان:</strong> واضح أن $f(x)$ هو تركيب الدالتين $y = g(x) , z = \sin y$
<br>
ومن قاعدة التسلسل نجد أن:
</div>

$$ \frac{dz}{dx} = \left(\frac{dz}{dy}\right)\left(\frac{dy}{dx}\right) $$
$$ = (\cos y) (g'(x)) \quad \text{لماذا؟} $$
$$ = \cos g(x) \cdot g'(x) $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4:</strong> أوجد مشتقة كل من الدوال الآتية عند قيمة $x$ المعطاة:
</div>

$$ (a) \quad y = \sin(2x+\pi) , \quad x = \frac{\pi}{2} $$
$$ (b) \quad y = x \sin \sqrt{x} , \quad x = \frac{\pi^2}{4} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(a)
</div>

$$ \because y = \sin(2x + \pi) $$
$$ \therefore \frac{dy}{dx} = (2) \cos(2x + \pi) $$
$$ \left(\frac{dy}{dx}\right)_{x=\frac{\pi}{2}} = (2) \cos\left(2\left(\frac{\pi}{2}\right) + \pi\right) $$
$$ = (2) \cos(2\pi) $$
$$ = (2)(1) $$
$$ = 2 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
(b)
</div>

$$ \because y = x \sin \sqrt{x} $$
$$ = x \sin(x)^{\frac{1}{2}} $$
$$ \therefore \frac{dy}{dx} = x \left[ \frac{1}{2} \left(\cos x^{\frac{1}{2}}\right) \left(x^{-\frac{1}{2}}\right) \right] + (1) \left(\sin x^{\frac{1}{2}}\right) $$
$$ = \frac{1}{2} x^{\frac{1}{2}} \cos x^{\frac{1}{2}} + \sin x^{\frac{1}{2}} $$
$$ = \frac{\sqrt{x} \cos \sqrt{x}}{2} + \sin \sqrt{x} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 2-1 مشتقات الدوال المثلثية
</div>
<!-- PAGE_END_27 -->


<!-- PAGE_START_28 -->
### صفحة 28

$$\therefore \left(\frac{dy}{dx}\right)_{x = \frac{\pi^2}{4}} = \frac{\sqrt{\frac{\pi^2}{4}} \cos \sqrt{\frac{\pi^2}{4}}}{2} + \sin \sqrt{\frac{\pi^2}{4}}$$

$$\frac{1}{2} = \frac{\left(\frac{\pi}{2}\right) \cos\left(\frac{\pi}{2}\right)}{2} + \sin\left(\frac{\pi}{2}\right)$$

$$= \frac{\pi(0)}{4} + 1$$

$$= 1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وتُعدُّ مشتقة دالة الجيب هي الأساس في دراستنا لمشتقات الدوال المثلثية الأخرى، حيث إن مشتقات بقية الدوال المثلثية جميعها نتائج منها:
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة (3):</strong>
<br>
إذا كانت:
$$f(x) = \cos x$$
فإن:
$$f'(x) = -\sin x$$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان:</strong>
</div>

$$\therefore f(x) = \cos x , \quad \cos x = \sin\left(\frac{\pi}{2} - x\right)$$

$$\therefore f(x) = \sin\left(\frac{\pi}{2} - x\right)$$

$$\therefore f'(x) = \cos\left(\frac{\pi}{2} - x\right)(-1)$$

$$= -\sin x$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة (4):</strong>
<br>
إذا كانت:
$$f(x) = \cos (g(x))$$
فإن:
$$f'(x) = -\sin (g(x)) (g'(x))$$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
البرهان مماثل لبرهان نتيجة (2).
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 1 الاشتقاق | 28
</div>
<!-- PAGE_END_28 -->


<!-- PAGE_START_29 -->
### صفحة 29

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5:</strong> إذا كان $f(x) = \cos \frac{1}{2} x$ ، فأوجد $f'\left(\frac{\pi}{2}\right)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because f(x) = \cos \frac{1}{2} x $$

$$ \therefore f'(x) = \left( -\sin \frac{1}{2} x \right) \left( \frac{1}{2} \right) $$

$$ = -\frac{1}{2} \sin \frac{1}{2} x $$

$$ \therefore f'\left(\frac{\pi}{2}\right) = -\frac{1}{2} \sin \frac{1}{2} \left(\frac{\pi}{2}\right) $$

$$ = -\frac{1}{2} \sin \frac{\pi}{4} $$

$$ = -\frac{1}{2} \left( \frac{1}{\sqrt{2}} \right) $$

$$ = -\frac{1}{2 \sqrt{2}} $$

$$ = -\frac{\sqrt{2}}{4} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة 5:</strong>
<br>
إذا كانت:
<br>
$f(x) = \tan x , x \neq \frac{\pi}{2} + n\pi , n \in \mathbb{Z}$
<br>
فإن:
$$ f'(x) = \sec^2 x $$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان:</strong>
</div>

$$ \because f(x) = \tan x $$

$$ = \frac{\sin x}{\cos x} , x \neq \frac{\pi}{2} + n\pi , n \in \mathbb{Z} $$

$$ \therefore f'(x) = \frac{\cos x \cos x - \sin x (-\sin x)}{(\cos x)^2} $$

$$ = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} $$

$$ = \frac{1}{\cos^2 x} \quad \text{لماذا؟} $$

$$ = \sec^2 x $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 1-2 مشتقات الدوال المثلثية | <strong>29</strong>
</div>
<!-- PAGE_END_29 -->


<!-- PAGE_START_30 -->
### صفحة 30

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة (6)</strong>
<br>
إذا كانت:
$$f(x) = \tan(g(x))$$
فإن:
$$f'(x) = \sec^2(g(x)) (g'(x))$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
البرهان مماثل لبرهان نتيجة (2).
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (6)</strong>
<br>
إذا كانت $f(x) = 2x^2 \tan 2x$ ، فأوجد $f'(0)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because f(x) = 2x^2 \tan 2x$$

$$\therefore f'(x) = [(2x^2 \sec^2 2x) (2)] + [(\tan 2x)(4x)]$$

$$= 4x^2 \sec^2 2x + 4x \tan 2x$$

$$= 4x (x \sec^2 2x + \tan 2x)$$

$$\therefore f'(0) = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب (1)</strong>
<br>
أوجد $f'(x)$ لكل دالة مما يأتي:
<br>
a) $f(x) = \sin^2 3x$
<br>
b) $f(x) = \cos x^3$
<br>
c) $f(x) = x \tan x$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>الفصل 1 الاشتقاق</strong> | <strong>30</strong>
</div>
<!-- PAGE_END_30 -->


<!-- PAGE_START_31 -->
### صفحة 31

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة</strong><br>
إذا كانت:
</div>

$$f(x) = \sec x, \quad x \neq \frac{\pi}{2} + n\pi, \, n \in \mathbb{Z}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فإن:
</div>

$$f'(x) = \sec x \tan x$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان</strong>
</div>

$$\because f(x) = \sec x = \frac{1}{\cos x}$$

$$\therefore f'(x) = \frac{[(\cos x) (0)] - [(1) (-\sin x)]}{(\cos x)^2}$$

$$= \frac{\sin x}{\cos^2 x}$$

$$= \left(\frac{1}{\cos x}\right) \left(\frac{\sin x}{\cos x}\right)$$

$$= \sec x \tan x$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 7</strong><br>
إذا كانت $f(x) = \sec^4 (3x)$، فأوجد $f'\left(\frac{\pi}{12}\right)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because f(x) = (\sec 3x)^4$$

$$\therefore f'(x) = 4 (\sec 3x)^3 (\sec 3x) (\tan 3x) (3)$$

$$= 12 (\sec 3x)^4 (\tan 3x)$$

$$\therefore f'\left(\frac{\pi}{12}\right) = 12 \left(\sec 3\left(\frac{\pi}{12}\right)\right)^4 \left(\tan 3\left(\frac{\pi}{12}\right)\right)$$

$$= 12 \left(\sec \frac{\pi}{4}\right)^4 \left(\tan \frac{\pi}{4}\right)$$

$$= 12 (\sqrt{2})^4 (1)$$

$$= 12 (4)$$

$$= 48$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 2-1 مشتقات الدوال المثلثية
</div>
31
<!-- PAGE_END_31 -->


<!-- PAGE_START_32 -->
### صفحة 32

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة (8):</strong><br>
إذا كانت:
$$f(x) = \csc x , \quad x \neq n\pi , \; n \in \mathbb{Z}$$
فإن:
$$f'(x) = -\csc x \cot x$$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان:</strong>
$$\because f(x) = \csc x = \frac{1}{\sin x}$$
$$\therefore f'(x) = \frac{[(\sin x) (0)] - [(1) (\cos x)]}{(\sin x)^2}$$
$$= \frac{-\cos x}{\sin^2 x}$$
$$= \left( \frac{-1}{\sin x} \right) \left( \frac{\cos x}{\sin x} \right)$$
$$= -\csc x \cot x$$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (8):</strong><br>
إذا كانت $f(x) = x^5 \csc x$ ، فأوجد $f'(x)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong style="color: #2b5b84;">الحل:</strong>
$$\because f(x) = x^5 \csc x$$
$$\therefore f'(x) = x^5 (-\csc x \cot x) + (5 x^4) \csc x$$
$$= x^4 \csc x (5 - x \cot x)$$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة (9):</strong><br>
إذا كانت:
$$f(x) = \cot x , \quad x \neq n\pi , \; n \in \mathbb{Z}$$
فإن:
$$f'(x) = -\csc^2 x$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الفصل 1 الاشتقاق <span style="float: left;">32</span>
</div>
<!-- PAGE_END_32 -->


<!-- PAGE_START_33 -->
### صفحة 33

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان</strong>
</div>

$$\because f(x) = \cot x = \frac{\cos x}{\sin x}$$

$$\therefore f'(x) = \frac{\sin x (-\sin x) - \cos x \cos x}{(\sin x)^2}$$

$$= \frac{-\sin^2 x - \cos^2 x}{\sin^2 x}$$

$$= \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x}$$

$$= \frac{-1}{\sin^2 x}$$

$$= -\csc^2 x$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 9</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذا كانت $f(x) = \cot \sqrt{x}$ ، فأوجد $f'\left(\frac{\pi^2}{4}\right)$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because f(x) = \cot \sqrt{x}$$

$$\therefore f'(x) = -\csc^2 x^{\frac{1}{2}} \left( \frac{1}{2} x^{-\frac{1}{2}} \right)$$

$$= \frac{-\csc^2 \sqrt{x}}{2\sqrt{x}}$$

$$\therefore f'\left(\frac{\pi^2}{4}\right) = \frac{-\csc^2 \sqrt{\frac{\pi^2}{4}}}{2\sqrt{\frac{\pi^2}{4}}}$$

$$= \frac{-\csc^2 \frac{\pi}{2}}{2\left(\frac{\pi}{2}\right)}$$

$$= \frac{-1}{\pi}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 2</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد $f'(x)$ لكل دالة مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $f(x) = \sec \frac{x}{3}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
b) $f(x) = x \csc 2x$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
c) $f(x) = \cot \frac{\pi}{x}$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 2-1 مشتقات الدوال المثلثية | 33
</div>
<!-- PAGE_END_33 -->


<!-- PAGE_START_34 -->
### صفحة 34

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 10:</strong> إذا كانت $g'(x) = \cos x$ , $f(x) = x^2$ ، فأوجد قيمة $[g \circ f]' \left( \sqrt{\frac{\pi}{3}} \right)$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because [g \circ f]'(x) = g'[f(x)] \cdot f'(x) $$

$$ g'(x) = \cos x \Rightarrow g'[f(x)] = \cos x^2 $$

$$ f(x) = x^2 \Rightarrow f'(x) = 2x $$

$$ \therefore [g \circ f]'(x) = \cos x^2 (2x) $$

$$ [g \circ f]' \left( \sqrt{\frac{\pi}{3}} \right) = \cos \left( \sqrt{\frac{\pi}{3}} \right)^2 \left( 2 \sqrt{\frac{\pi}{3}} \right) $$

$$ = 2 \cos \frac{\pi}{3} \left( \sqrt{\frac{\pi}{3}} \right) $$

$$ = 2 \left( \frac{1}{2} \right) \left( \sqrt{\frac{\pi}{3}} \right) $$

$$ = \sqrt{\frac{\pi}{3}} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 3:</strong> إذا كانت $g'(x) = x^3$ , $f(x) = \sin 4x$ ، فأوجد $[g \circ f]' \left( \frac{\pi}{16} \right)$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الجدول أدناه يُبيّن المشتقة الأولى للدوال المثلثية الست:
</div>

<br>

| $f(x)$ | $f'(x)$ | $f(x)$ | $f'(x)$ |
| :---: | :---: | :---: | :---: |
| $\sin x$ | $\cos x$ | $\sin(g(x))$ | $\cos(g(x)) \cdot g'(x)$ |
| $\cos x$ | $-\sin x$ | $\cos(g(x))$ | $-\sin(g(x)) \cdot g'(x)$ |
| $\tan x$ | $\sec^2 x$ | $\tan(g(x))$ | $\sec^2(g(x)) \cdot g'(x)$ |
| $\sec x$ | $\sec x \tan x$ | $\sec(g(x))$ | $\sec(g(x)) \cdot \tan(g(x)) \cdot g'(x)$ |
| $\csc x$ | $-\csc x \cot x$ | $\csc(g(x))$ | $-\csc(g(x)) \cdot \cot(g(x)) \cdot g'(x)$ |
| $\cot x$ | $-\csc^2 x$ | $\cot(g(x))$ | $-\csc^2(g(x)) \cdot g'(x)$ |

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الفصل 1 الاشتقاق | <strong>34</strong>
</div>
<!-- PAGE_END_34 -->


<!-- PAGE_START_35 -->
### صفحة 35

<div dir="rtl" style="text-align: center; font-size: 20px; font-weight: bold;">
تمارين 1-2
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px; font-weight: bold;">
أوجد مشتقة كلّ من الدوال الآتية:
</div>

$$1) \quad y = \sin 2x$$

$$2) \quad f(x) = \tan \sqrt{x+1}$$

$$3) \quad f(x) = \cos (4x^2 - 1)$$

$$4) \quad y = 5x \cot 5x$$

$$5) \quad y = \sqrt{\sec x}$$

$$6) \quad f(x) = \cos 6x \csc 6x$$

$$7) \quad f(x) = 1 + \frac{1 + \sin x}{\cos x}$$

$$8) \quad y = \frac{\sin x}{2 + \csc x}$$

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px; font-weight: bold;">
أوجد مشتقة كلّ من الدوال الآتية عند قيمة $x$ المعطاة:
</div>

$$9) \quad f(x) = x \cos x \ , \ x = \pi$$

$$10) \quad f(x) = \cot^3 x \ , \ x = \frac{\pi}{4}$$

$$11) \quad f(x) = (\sin 2x + \cos 2x)^2 \ , \ x = \frac{3\pi}{2}$$

$$12) \quad f(x) = \frac{\tan x}{x + 1} \ , \ x = 0$$

$$13) \quad f(x) = \frac{\csc x}{2 + \cot x} \ , \ x = \frac{\pi}{2}$$

$$14) \quad f(x) = \frac{1 + \sec 4x}{1 - 2 \sec 4x} \ , \ x = \frac{\pi}{4}$$

$$15) \quad f(x) = \frac{1 - \sin x}{1 + \sin x} \ , \ x = \pi$$

$$16) \quad f(x) = x \tan x^2 \ , \ x = \sqrt{\pi}$$

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
17) إذا كانت $f(x) = \sin x - \frac{1}{3} \sin^3 x$ ، فأثبت أن $f'(x) = \cos^3 x$
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
18) إذا كانت $g(x) = \sin x \ , \ f(x) = x^2 - \frac{\pi}{4}$ ، فأوجد قيمة $[g \circ f]'(\sqrt{\pi})$ .
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
19) إذا كانت $g'(x) = \tan x \ , \ f(x) = x^3$ ، فأوجد قيمة $[g \circ f]'(x)$ .
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 2-1 مشتقات الدوال المثلثية | 35
</div>
<!-- PAGE_END_35 -->


<!-- PAGE_START_36 -->
### صفحة 36

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1>1-3 المشتقات العليا</h1>
<p><strong>Higher Order Derivatives</strong></p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
تعلم أنه إذا كانت $y = f(x)$ دالة، فإن المشتقة الأولى لها هي $f'(x)$، وهي أيضاً دالة في $x$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
وإذا كانت الدالة $f'(x)$ قابلة للاشتقاق، فإن مشتقها تسمى (المشتقة الثانية) أو (مشتقة المشتقة)، ويرمز لها بالرمز $f''(x)$ ، أو $\frac{d^2 y}{dx^2}$ ، أو $\frac{d^2}{dx^2} f(x)$ . كما أنه إذا كانت المشتقة الثانية دالة قابلة للاشتقاق، فإن مشتقة المشتقة الثانية هي المشتقة الثالثة للدالة $y = f(x)$ ، ويرمز لها بالرمز $f'''(x)$ ، أو $\frac{d^3 y}{dx^3}$ ، أو $\frac{d^3}{dx^3} (f(x))$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبصورة عامة، فإن نتيجة اشتقاق الدالة $y = f(x)$ من $n$ من المرات المتتالية تسمى (المشتقة النونية) للدالة $y = f(x)$ ، ويرمز لها بالرمز $\frac{d^n y}{dx^n}$ ، أو $\frac{d^n}{dx^n} (f(x))$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>مثال 1</h3>
إذا كانت $f(x) = x^4 - 2x^{-3} + \frac{1}{2} x^2 + 8$ ، فأوجد $f'(x), f''(x), f'''(x)$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because f(x) = x^4 - 2x^{-3} + \frac{1}{2} x^2 + 8$$

$$\therefore f'(x) = 4x^3 + 6x^{-4} + x$$

$$f''(x) = 12x^2 - 24x^{-5} + 1$$

$$f'''(x) = 24x + 120x^{-6}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>تدريب 1</h3>
في مثال (1) أوجد $\frac{d^5}{dx^5} (f(x))$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
36 الفصل 1 الاشتقاق
</div>
<!-- PAGE_END_36 -->


<!-- PAGE_START_37 -->
### صفحة 37

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 2</strong>
<br>
إذا كانت $y = \cos x$ ، فأثبت أن $\left(\frac{dy}{dx}\right)^2 - y \frac{d^2y}{dx^2} = 1$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = \cos x$$
$$\therefore \frac{dy}{dx} = -\sin x$$
$$\frac{d^2y}{dx^2} = -\cos x$$
$$\text{L.H.S} = \left(\frac{dy}{dx}\right)^2 - y \left(\frac{d^2y}{dx^2}\right)$$
$$= (-\sin x)^2 - y(-\cos x)$$
$$= \sin^2 x + (\cos x)(\cos x)$$
$$= \sin^2 x + \cos^2 x$$
$$= 1$$
$$= \text{R.H.S}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 2</strong>
<br>
إذا كانت $y = \cos x$ ، فأثبت أن $\frac{d^4y}{dx^4} = y$ .
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3</strong>
<br>
إذا كانت $f(x) = x^2 + \frac{k}{x} \, , \, k \in \mathbb{R}$ ، فأوجد قيمة $k$ إذا كانت $f''(x) = 0$ ، عندما $x = 1$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because f(x) = x^2 + \frac{k}{x}$$
$$\therefore f'(x) = 2x - \frac{k}{x^2}$$
$$f''(x) = 2 - \left(\frac{-2x\,k}{x^4}\right)$$
$$= 2 + \frac{2k}{x^3}$$
$$\because f''(x) = 0 \text{ عندما } x = 1$$
$$\therefore f''(1) = 2 + \frac{2k}{1} = 0 \Rightarrow 2k = -2$$
$$\therefore k = -1$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>37</strong> | الدرس 3-1 المشتقات العليا
</div>
<!-- PAGE_END_37 -->


<!-- PAGE_START_38 -->
### صفحة 38

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4</strong><br>
إذا كانت $f'(x) = \cos x^2 , g(x) = 3x$ ، فأوجد قيمة $[f \circ g]''(x)$ ، عندما $x = \frac{\sqrt{\pi}}{3}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: blue; font-weight: bold;">الحل</span>
</div>

$$ \because [f \circ g]'(x) = f'[g(x)] \cdot g'(x) , $$

$$ f'(x) = \cos x^2 , \quad g(x) = 3x $$

$$ \therefore [f \circ g]'(x) = \cos(3x)^2 (3) $$

$$ = 3 \cos 9x^2 $$

$$ [f \circ g]''(x) = 3 (-\sin 9x^2)(18x) $$

$$ = -54x \sin 9x^2 $$

$$ [f \circ g]''\left(\frac{\sqrt{\pi}}{3}\right) = -54 \left(\frac{\sqrt{\pi}}{3}\right) \sin 9\left(\frac{\pi}{9}\right) $$

$$ = -18\sqrt{\pi} \sin \pi $$

$$ = 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">لماذا؟ 0</span>
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5</strong><br>
إذا كانت $f(x) = \sin x , g(x) = x^2$ ، فأوجد قيمة $[f \circ g]''(x)$ ، عندما $x = \sqrt{\frac{\pi}{2}}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: blue; font-weight: bold;">الحل</span>
</div>

$$ \because f(x) = \sin x , \quad g(x) = x^2 $$

$$ \therefore [f \circ g](x) = f[g(x)] = \sin x^2 $$

$$ [f \circ g]'(x) = 2x \cos x^2 $$

$$ [f \circ g]''(x) = 2x (-\sin x^2 (2x)) + 2 \cos x^2 $$

$$ = -4x^2 \sin x^2 + 2 \cos x^2 $$

$$ [f \circ g]''\left(\sqrt{\frac{\pi}{2}}\right) = -4 \left(\sqrt{\frac{\pi}{2}}\right)^2 \sin \left(\sqrt{\frac{\pi}{2}}\right)^2 + 2 \cos \left(\sqrt{\frac{\pi}{2}}\right)^2 $$

$$ = -4 \left(\frac{\pi}{2}\right) \sin \frac{\pi}{2} + 2 \cos \frac{\pi}{2} $$

$$ = -2\pi (1) + 0 $$

$$ = -2\pi $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
38 <strong>الفصل 1</strong> الاشتقاق
</div>
<!-- PAGE_END_38 -->


<!-- PAGE_START_39 -->
### صفحة 39

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2><b>تمارين 1-3</b></h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">1</span> أوجد المشتقة الثانية والثالثة لكل دالة مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $f(x) = \frac{2}{3}x^3 + 2x^{-2} - 3x + 6$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
b) $f(x) = 3x \sin x$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
c) $f(x) = \frac{x^2 + 1}{x}$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">2</span> إذا كانت $y = \sec 2x$ ، فأثبت أن $\frac{d^2y}{dx^2} + 4y = 8y^3$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">3</span> إذا كانت $h(x) = \cos ax - \sin ax$ ، حيث $a \in \mathbb{R}$ ، فأثبت أن $h''(x) + a^2 h(x) = 0$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">4</span> إذا كانت $y = \sin x + 2$ ، فأوجد $\frac{d^3y}{dx^3} + \frac{d^2y}{dx^2} + \frac{dy}{dx} + y$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">5</span> إذا كانت $y = x \tan x$ ، فأثبت أن $\frac{d^2y}{dx^2} = 2(1 + y)\sec^2 x$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">6</span> إذا كانت $g(x) = \sin x , f(x) = x^3$ ، فأوجد $[g \circ f]''(x)$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">7</span> إذا كانت $g(x) = 2x , f'(x) = \csc x$ ، فأوجد $[g \circ f]''(x)$ .
</div>

<br><br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>39</b> &nbsp;&nbsp;&nbsp;&nbsp; <b>الدرس 1-3</b> المشتقات العليا
</div>
<!-- PAGE_END_39 -->


<!-- PAGE_START_40 -->
### صفحة 40

<div dir="rtl" style="text-align: right; font-size: 16px;">
اختبار الفصل 1
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد $\frac{dy}{dx}$ لكلّ مما يأتي:
</div>

$$y = 2z - \frac{1}{z} , \quad z = 7x - 2 , \quad x \neq \frac{2}{7} \tag{1}$$

$$\frac{dy}{dz} = 3z^2 - 7 , \quad z = 8x^3 + 5 \tag{2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد $\frac{dy}{dx}$ عند قيمة $x$ المعطاة:
</div>

$$y = \frac{1}{z+6} , \quad z = 3x^2 - 1 , \quad x = -1 \tag{3}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد $[f \circ g]'(x)$ لكلّ دالة مما يأتي:
</div>

$$f(x) = x^2 - 5x + 3 , \quad g(x) = 6x + 1 \tag{4}$$

$$f'(x) = \frac{1}{x^2} , \quad g(x) = 4x - 3 , \quad x \neq \frac{3}{4} \tag{5}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد $\frac{dy}{dx}$ لكلّ دالة مما يأتي:
</div>

$$y = \frac{9}{\sqrt{x^2 + 16}} \tag{6}$$

$$y = x^5 (x^2 + 3)^{-1} \tag{7}$$

$$y = \left(\frac{1+x}{x-3}\right)^8 , \quad x \neq 3 \tag{8}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(9) إذا كان $(5x - 3)^2 = (y + 2)^3$ ، فأثبت أن $100 = 9(y + 2)\left(\frac{dy}{dx}\right)^2$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(10) إذا كان $\frac{x^2}{25} - \frac{y^2}{9} = 1$ ، فأثبت أن $\frac{dy}{dx} = \frac{9x}{25y}$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
(11) إذا كان $x^2 - 5xy - y^2 = 7$ ، فأوجد $\frac{dy}{dx}$ عند النقطة $(1, -2)$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 1 الاشتقاق | 40
</div>
<!-- PAGE_END_40 -->
