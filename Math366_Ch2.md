

<!-- PAGE_START_44 -->
### صفحة 44

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>2-1 تطبيقات هندسية</h2>
<b>Geometrical Applications</b>
<br><br>
للمشتقة تطبيقات عديدة منها الهندسية والتي تمكننا من إيجاد معادلة المماس والعمودي لمنحنى الدالة $y = f(x)$ عند أي نقطة $(x_1, y_1)$ واقعة عليه، وسنقدم فيما يأتي مراجعة لبعض المفاهيم.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>ميل المستقيم</h3>
يبيّن الشكل المجاور المستقيم $KL$ الذي يصنع زاوية قياسها $\theta$ مع الاتجاه الموجب للمحور $x$، ويمكنك ملاحظة أن ميل المستقيم $KL$ هو
</div>

$$m = \frac{y_2 - y_1}{x_2 - x_1}, \quad x_1 \neq x_2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وحيث أن $y_2 - y_1$ يمثل المقابل للزاوية $\theta$، و $x_2 - x_1$ يمثل المجاور لها في المثلث القائم الزاوية $KLN$، فإن
</div>

$$m = \tan \theta, \quad 0 \le \theta < \pi$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويكون المستقيم $KL$ أفقياً (موازياً للمحور $x$) عندما $m = 0$، ويصنع المستقيم $KL$ زاوية حادة مع الاتجاه الموجب للمحور $x$ عندما $m > 0$، ويصنع زاوية منفرجة مع الاتجاه الموجب للمحور $x$ عندما $m < 0$. ويكون المستقيم $KL$ رأسياً (موازياً للمحور $y$)، عندما يكون ميله غير معرّف.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>معادلة المستقيم</h3>
تذكّر أن:
<ul>
<li>معادلة المستقيم الذي ميله $m$، ويمر بالنقطة $(x_1, y_1)$ هي:</li>
</ul>
</div>

$$y - y_1 = m(x - x_1)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<ul>
<li>معادلة المستقيم الذي ميله $m$، ومقطعه من المحور $y$ هو $b$، هي:</li>
</ul>
</div>

$$y = mx + b$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<ul>
<li>الصورة العامة لمعادلة المستقيم هي:</li>
</ul>
</div>

$$ax + by + c = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن هذه المعادلة يمكنك أن تجد أن الميل $m = -\frac{a}{b}$.
<ul>
<li>إذا كان $m_1 , m_2$ ميلي المستقيمين $l_1 , l_2$ على الترتيب، فإن:</li>
</ul>
</div>

$$m_1 = m_2 \iff \overleftrightarrow{l_1} \parallel \overleftrightarrow{l_2}$$

$$m_1 \cdot m_2 = -1 \iff \overleftrightarrow{l_1} \perp \overleftrightarrow{l_2}$$

<br>

<div dir="rtl" style="text-align: left; font-size: 14px;">
<b>الفصل 2 تطبيقات المشتقة</b> &nbsp;&nbsp;&nbsp;&nbsp; <b>44</b>
</div>
<!-- PAGE_END_44 -->


<!-- PAGE_START_45 -->
### صفحة 45

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="text-align: center; color: #8b0000;">المعنى الهندسي للمشتقة الأولى</h3>

الشكل المجاور يُمثّل منحنى الدالة $y = f(x)$، افرض أن هذا المنحنى يمر بالنقطتين $A, B$
حيث $A(x_0, f(x_0)), B(x_0+h, f(x_0+h))$،
وميل الوتر $\overline{AB}$ يرمز له بالرمز $m$، فإن:
</div>

$$m = \frac{f(x_0+h) - f(x_0)}{(x_0+h) - x_0}, \quad h \neq 0$$
$$= \frac{f(x_0+h) - f(x_0)}{h}, \quad h \neq 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وإذا تحركت النقطة $B$ مقتربة من النقطة $A$ قربًا كافيًا، فإن الوتر $\overline{AB}$ يصبح مماسًا لمنحنى الدالة عند النقطة $A$، $h \to 0$ عند هذه اللحظة. وبافتراض أن ميل المماس $m$، فإن:
</div>

$$m = \lim_{h \to 0} \frac{f(x_0+h) - f(x_0)}{h}$$
$$= f'(x_0)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وحيث إن المماس يصنع زاوية موجبة قياسها $\theta$ مع الاتجاه الموجب للمحور $x$، فإن:
</div>

$$m = \tan \theta$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويمكننا أن نوجز على النحو الآتي:
ميل المماس لمنحنى الدالة $y = f(x)$ عند النقطة $(x_0, f(x_0))$ هو $m$، حيث:
</div>

$$m = \lim_{h \to 0} \frac{f(x_0+h) - f(x_0)}{h} = f'(x_0) = \tan \theta, \quad h \neq 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
تسمى النقطة $(x_0, f(x_0))$ بنقطة التماس، وتكون الدالة $f(x)$ قابلة للاشتقاق عند النقطة $(x_0, f(x_0))$ إذا وفقط إذا أمكن رسم مماس وحيد لمنحنى الدالة عند هذه النقطة، ويكون ميل المماس عند $x_0$ مساويًا لقيمة المشتقة، مع ملاحظة أنه:

• إذا كانت $f'(x_0) > 0$، فإن ميل المماس لمنحنى الدالة $f(x)$ يكون موجبًا؛ أي أن المماس يصنع زاوية حادة مع الاتجاه الموجب للمحور $x$، وفي هذه الحالة تكون الدالة تزايدية.

• إذا كانت $f'(x_0) < 0$، فإن ميل المماس لمنحنى الدالة $f(x)$ يكون سالبًا؛ أي أن المماس يصنع زاوية منفرجة مع الاتجاه الموجب للمحور $x$، وفي هذه الحالة تكون الدالة تناقصية.

• إذا كانت $f'(x_0) = 0$، فإن ميل المماس لمنحنى الدالة $f(x)$ يساوي صفرًا؛ أي أن المماس لمنحنى الدالة $f(x)$ عند النقطة $(x_0, f(x_0))$ يكون موازيًا للمحور $x$ (المماس أفقيًا).

• إذا كانت $f'(x_0)$ (كمية غير معرّفة)، فإن المماس لمنحنى الدالة $f(x)$ عند النقطة $(x_0, f(x_0))$ يكون موازيًا للمحور $y$ (المماس رأسيًا).
</div>

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 1-2 تطبيقات هندسية | 45
</div>
<!-- PAGE_END_45 -->


<!-- PAGE_START_46 -->
### صفحة 46

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1</strong>
<br>
بيّن متى تكون الدالة $y = x^2$ متزايدة، ومتى تكون متناقصة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = x^2$$

$$\therefore \frac{dy}{dx} = 2x$$

$$\text{تكون } \frac{dy}{dx} > 0 \text{ عندما } x > 0$$

$$\text{وتكون } \frac{dy}{dx} < 0 \text{ عندما } x < 0 \text{؛}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن الدالة متزايدة
</div>

$$\forall x > 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومتناقصة
</div>

$$\forall x < 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 2</strong>
<br>
أوجد ميل المماس لمنحنى $f(x)$ عند قيم $x$ المعطاة في كل مما يأتي:
<br>
a) $f(x) = \frac{x+3}{x+1} , x \neq -1 , x = 1 , x = -\frac{3}{2}$
<br>
b) $f(x) = |x - 1| , x = \frac{1}{2} , x = 2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\text{a) } \because f(x) = \frac{x+3}{x+1}$$

$$\therefore f'(x) = \frac{(x+1) (1) - (x+3) (1)}{(x+1)^2}$$

$$= \frac{-2}{(x+1)^2}$$

$$f'(1) = \frac{-2}{(1+1)^2} = -\frac{1}{2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ ميل المنحنى $(m)$ يساوي $-\frac{1}{2}$ عند $x = 1$؛ أي أن $m = -\frac{1}{2}$
</div>

$$f'\left(-\frac{3}{2}\right) = \frac{-2}{\left(-\frac{3}{2} + 1\right)^2} = -8$$

$$\therefore m = -8$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
46 &nbsp;&nbsp;&nbsp;&nbsp; <strong>الفصل 2</strong> تطبيقات المشتقة
</div>
<!-- PAGE_END_46 -->

<!-- PAGE_START_47 -->
### صفحة 47

<div dir="rtl" style="text-align: right; font-size: 16px;">
$$\text{b) } \because f(x) = |x - 1|$$

$$\therefore f(x) = \begin{cases} x - 1 & , & x \ge 1 \\ 1 - x & , & x < 1 \end{cases}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = \frac{1}{2}$ ، فإن:
</div>

$$f(x) = 1 - x$$
$$f'(x) = -1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ ميل المنحنى $m$ يساوي $-1$ عندما $x = \frac{1}{2}$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = 2$ ، فإن:
</div>

$$f(x) = x - 1$$
$$f'(x) = 1$$

$$\therefore m = 1$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (3)</strong><br>
أوجد النقاط الواقعة على منحنى $y = \frac{2}{3}x^3 - \frac{9}{2}x^2 + 7x + \frac{3}{2}$ والتي يصنع المماس عندها زاوية ظلها يساوي $(-2)$ مع الاتجاه الموجب للمحور $x$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = \frac{2}{3}x^3 - \frac{9}{2}x^2 + 7x + \frac{3}{2}$$

$$\therefore \frac{dy}{dx} = 2x^2 - 9x + 7$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ المماس يصنع مع الاتجاه الموجب للمحور $x$ زاوية ظلها يساوي $(-2)$ .
</div>

$$\therefore \frac{dy}{dx} = \tan \theta = -2$$

$$2x^2 - 9x + 7 = -2$$

$$2x^2 - 9x + 9 = 0$$

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
47 | الدرس 1-2 تطبيقات هندسية
</div>
<!-- PAGE_END_47 -->



<!-- PAGE_START_48 -->
### صفحة 48

$$ (2x - 3) (x - 3) = 0 $$
$$ x = 3 \quad \text{أو} \quad x = \frac{3}{2} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = \frac{3}{2}$ ، فإن:
</div>

$$ y = \frac{2}{3} \left( \frac{3}{2} \right)^3 - \frac{9}{2} \left( \frac{3}{2} \right)^2 + 7 \left( \frac{3}{2} \right) + \frac{3}{2} = \frac{33}{8} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = 3$ ، فإن:
</div>

$$ y = \frac{2}{3} (3)^3 - \frac{9}{2} (3)^2 + 7 (3) + \frac{3}{2} = 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ المماس لمنحنى الدالة يصنع مع الاتجاه الموجب لمحور $x$ زاوية ظلها يساوي $(-2)$ عند النقطتين $\left( \frac{3}{2} , \frac{33}{8} \right)$ ، $(3 , 0)$ .
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4:</strong> أوجد النقاط الواقعة على منحنى $f(x) = \frac{x^2 - 3}{x + 2}$ ، والتي يكون المماس عندها موازيًا لمحور $x$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because f(x) = \frac{x^2 - 3}{x + 2} $$
$$ \therefore f'(x) = \frac{(x + 2)(2x) - (x^2 - 3)(1)}{(x + 2)^2} $$
$$ = \frac{x^2 + 4x + 3}{(x + 2)^2} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ المماس موازٍ لمحور $x$
</div>

$$ \therefore f'(x) = 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن:
</div>

$$ x^2 + 4x + 3 = 0 $$
$$ (x + 3)(x + 1) = 0 $$
$$ \therefore x = -3 \quad \text{أو} \quad x = -1 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = -3$ ، فإن:
</div>

$$ f(-3) = \frac{9 - 3}{-3 + 2} = -6 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = -1$ ، فإن:
</div>

$$ f(-1) = \frac{(-1)^2 - 3}{-1 + 2} = -2 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ المماس لمنحنى الدالة $f(x)$ يكون موازيًا لمحور $x$ عند النقطتين $(-1 , -2)$ ، $(-3 , -6)$ .
</div>

---
<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 2 تطبيقات المشتقة | 48
</div>
<!-- PAGE_END_48 -->


<!-- PAGE_START_49 -->
### صفحة 49

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 1:</strong><br>
أوجد النقاط الواقعة على منحنى $y = -x^2 + 4x + 3$ والتي يكون المماس عندها:
<br>
a) موازياً للمحور $x$.
<br>
b) يصنع مع الاتجاه الموجب للمحور $x$ زاوية قياسها $\frac{3\pi}{4}$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5:</strong><br>
أوجد قياس الزاوية التي يصنعها المماس لمنحنى $f(x) = \frac{x - 3}{x + 1}$ مع الاتجاه الموجب للمحور $x$ عند النقطة $(1, -1)$ الواقعة على المنحنى.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because f(x) = \frac{x - 3}{x + 1}$$

$$\therefore f'(x) = \frac{(x + 1)(1) - (x - 3)(1)}{(x + 1)^2}$$

$$= \frac{4}{(x + 1)^2}$$

$$f'(1) = \frac{4}{(1 + 1)^2} = 1$$

$$f'(x) = \tan\theta$$

$$\therefore \tan\theta = f'(1) = 1$$

$$\therefore m\angle\theta = \frac{\pi}{4}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 6:</strong><br>
أوجد النقاط الواقعة على منحنى $y = x^3 - 3x - 2$ ، والتي يكون المماس لمنحنى الدالة عندها موازياً للمستقيم الذي معادلته $y + 3x - 7 = 0$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because y = x^3 - 3x - 2$$

$$\therefore \frac{dy}{dx} = 3x^2 - 3$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
49 | الدرس 1-2 تطبيقات هندسية
</div>
<!-- PAGE_END_49 -->


<!-- PAGE_START_50 -->
### صفحة 50

<div dir="rtl" style="text-align: right; font-size: 16px;">
بفرض أن ميل المستقيم المعلوم $m_1$
</div>

$$m_1 = \frac{-a}{b} = -3$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ المماس لمنحنى الدالة يوازي المستقيم المعلوم، وبافتراض أن ميل المماس $m_2$
</div>

$$\therefore m_1 = m_2 = -3$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ ميل المماس يساوي قيمة المشتقة الأولى للدالة $y = f(x)$
</div>

$$\therefore 3x^2 - 3 = -3$$

$$x^2 = 0$$

$$x = 0 \Rightarrow y = -2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ المماس لمنحنى الدالة $y = f(x)$ يكون موازياً للمستقيم $y + 3x - 7 = 0$ عند النقطة $(0, -2)$.
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: #c00000; margin-bottom: 5px;">معادلة المماس لمنحنى دالة</h3>
بفرض أن النقطة $A(x_1, y_1)$ تقع على منحنى $y = f(x)$، فإن ميل المماس لمنحنى الدالة $y = f(x)$ عند النقطة $A(x_1, y_1)$ هو:
</div>

$$m = \left(\frac{dy}{dx}\right)_{(x_1, y_1)}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
معادلة المماس لمنحنى $y = f(x)$ عند النقطة $(x_1, y_1)$ الواقعة عليه هي:
</div>

$$y - y_1 = f'(x_1)(x - x_1) \quad \text{أو} \quad y - y_1 = \left(\frac{dy}{dx}\right)_{(x_1, y_1)}(x - x_1)$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: #c00000; margin-bottom: 5px;">معادلة العمودي على المنحنى</h3>
نحتاج في بعض الأحيان لإيجاد معادلة العمودي على المنحنى عند نقطة ما عليه، والعمودي على منحنى ما عند أي نقطة واقعة عليه هو العمودي على مماس المنحنى عند تلك النقطة ، وحيث إن ميل المماس لمنحنى $y = f(x)$ عند النقطة $(x_1, y_1)$ هو:
</div>

$$m = \left(\frac{dy}{dx}\right)_{(x_1, y_1)}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فإن ميل العمودي عليه هو:
</div>

$$\frac{-1}{\left(\frac{dy}{dx}\right)_{(x_1, y_1)}}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ معادلة العمودي على المنحنى $y = f(x)$ عند النقطة $(x_1, y_1)$ الواقعة عليه هي:
</div>

$$y - y_1 = \frac{-1}{f'(x_1)}(x - x_1) \quad \text{أو} \quad y - y_1 = \frac{-1}{\left(\frac{dy}{dx}\right)_{(x_1, y_1)}}(x - x_1)$$

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>50</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>الفصل 2 تطبيقات المشتقة</b>
</div>
<!-- PAGE_END_50 -->


<!-- PAGE_START_51 -->
### صفحة 51

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (7):</strong><br>
أوجد معادلة المماس لمنحنى $y = x^3 - 3x^2 + 5$ ، عند النقطة $(1, 3)$ الواقعة عليه.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because y = x^3 - 3x^2 + 5 $$

$$ \therefore \frac{dy}{dx} = 3x^2 - 6x $$

$$ \therefore m = \left(\frac{dy}{dx}\right)_{(x_1, y_1)} = 3(1) - 6(1) = -3 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ معادلة المماس هي:
</div>

$$ y - y_1 = \left(\frac{dy}{dx}\right)_{(x_1, y_1)} (x - x_1) $$

$$ \therefore y - 3 = -3 (x - 1) $$

$$ 3x + y - 6 = 0 $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (8):</strong><br>
أوجد معادلتي المماس والعمودي لمنحنى $y = x^3 - 2x^2 + 4$ عند النقطة $(2, 4)$ الواقعة عليه.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because y = x^3 - 2x^2 + 4 $$

$$ \therefore \frac{dy}{dx} = 3x^2 - 4x $$

$$ \because m = \left(\frac{dy}{dx}\right)_{(2, 4)} = 3(4) - 4(2) = 4 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ معادلة المماس هي:
</div>

$$ y - y_1 = f'(x_1)(x - x_1) $$

$$ \therefore y - 4 = 4(x - 2) $$

$$ 4x - y - 4 = 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ معادلة العمودي هي:
</div>

$$ y - y_1 = \frac{-1}{f'(x_1)} (x - x_1) $$

$$ \therefore y - 4 = \frac{-1}{4} (x - 2) $$

$$ x + 4y - 18 = 0 $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب (2):</strong><br>
أوجد النقاط الواقعة على منحنى $y = x^2 - 7x + 3$ ، والتي يكون المماس عندها:<br>
<strong>a)</strong> موازياً للمستقيم $5x + y - 3 = 0$<br>
<strong>b)</strong> عمودياً على المستقيم $2x + 4y = 1$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 1-2 تطبيقات هندسية | <strong>51</strong>
</div>
<!-- PAGE_END_51 -->


<!-- PAGE_START_52 -->
### صفحة 52

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 9:</b> أوجد معادلة المماس لمنحنى $x^2 + y^2 + 3x - 4y = 1$ عند النقطة $(1, 3)$ الواقعة عليه.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل:</b>
</div>

$$\because x^2 + y^2 + 3x - 4y = 1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة إلى $x$
</div>

$$\therefore 2x + 2y \frac{dy}{dx} + 3 - 4 \frac{dy}{dx} = 0$$

$$\frac{dy}{dx} (2y - 4) = -3 - 2x$$

$$\frac{dy}{dx} = \frac{-3 - 2x}{(2y - 4)}$$

$$\because m = \left( \frac{dy}{dx} \right)_{(x_1, y_1)}$$

$$\therefore m = \left( \frac{dy}{dx} \right)_{(1, 3)}$$

$$= \frac{-3 - 2(1)}{2(3) - 4}$$

$$= \frac{-5}{2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ معادلة المماس هي:
</div>

$$y - y_1 = \left( \frac{dy}{dx} \right)_{(x_1, y_1)} (x - x_1)$$

$$\therefore y - 3 = \frac{-5}{2} (x - 1)$$

$$5x + 2y - 11 = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 10:</b> أوجد معادلة العمودي لمنحنى $y = x^2 + 2x - 3$ عند نقطة تقاطعه مع المستقيم $y = x - 1$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل:</b>
</div>

$$\because y = x^2 + 2x - 3 \quad , \quad y = x - 1$$

$$\therefore x^2 + 2x - 3 = x - 1$$

$$x^2 + x - 2 = 0$$

$$(x + 2)(x - 1) = 0$$

$$\therefore x = 1 \text{ أو } x = -2$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الفصل 2: تطبيقات المشتقة</b> | <b>52</b>
</div>
<!-- PAGE_END_52 -->


<!-- PAGE_START_53 -->
### صفحة 53

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = -2$ ، فإن $y = -3$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند $x = 1$ ، فإن $y = 0$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقطتا التقاطع هما $(-2, -3)$ ، $(1, 0)$
</div>

$$\because y = x^2 + 2x - 3$$
$$\therefore m = y' = 2x + 2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند النقطة $(-2, -3)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ ميل المماس هو $m$
</div>

$$\therefore m = y'|_{(-2, -3)}$$
$$= 2(-2) + 2 = -2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ ميل العمودي هو $\frac{-1}{m}$
</div>

$$\therefore \frac{-1}{m} = \frac{-1}{-2} = \frac{1}{2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
معادلة العمودي هي:
</div>

$$y - (-3) = \frac{1}{2}(x + 2)$$
$$x - 2y - 4 = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند النقطة $(1, 0)$
</div>

$$\because m = y'|_{(1, 0)}$$
$$= 2(1) + 2 = 4$$
$$\therefore \frac{-1}{m} = \frac{-1}{4}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
معادلة العمودي هي:
</div>

$$y - 0 = \frac{-1}{4}(x - 1)$$
$$x + 4y - 1 = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 1-2 تطبيقات هندسية 53
</div>
<!-- PAGE_END_53 -->


<!-- PAGE_START_54 -->
### صفحة 54

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2><b>تمارين 2-1</b></h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>أوجد ميل المماس لمنحنى كل مما يأتي عند قيمة $x$ أو النقطة المعطاة:</b>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
1) $y = 3x^3 - 5x^2 + 1 \quad, \quad x = \frac{1}{3}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2) $y = x + \frac{1}{x} \quad, \quad x = 1 \quad, \quad x \neq 0$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3) $y^2 = 10 - x^2 \quad, \quad (-1, 3)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
4) $xy^3 = 2 \quad, \quad x = 2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
5) $y = x^2 + 3|x| \quad, \quad x = -1$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
6) $y = \sqrt{x + 1} \quad, \quad (3, 2) \quad, \quad x \geq -1$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
7) $f(x) = \frac{3x - 1}{2x - 1} \quad, \quad (1, 2) \quad, \quad x \neq \frac{1}{2}$
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
8) أوجد النقاط الواقعة على منحنى $f(x) = x^3 - 3x$ التي يكون عندها المماس موازياً للمحور $x$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
9) أوجد قياس الزاوية الموجبة التي يصنعها المماس لمنحنى $y = f(x)$ مع المحور $x$ عند النقطة $(2, -3)$ الواقعة عليه، حيث $y = 2x^2 - 7x + 3$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
10) أوجد النقطة الواقعة على منحنى $y^2 - 4y - 2x - 1 = 0$ والتي يكون عندها المماس موازياً للمحور $y$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
11) أوجد النقطة الواقعة على منحنى $y = x^2 + 2$ والتي يصنع المماس عندها زاوية قياسها $\frac{3\pi}{4}$ مع الاتجاه الموجب للمحور $x$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
12) أوجد قيمتي $a , b$ ، إذا كان المماس لمنحنى $y = ax^2 + bx$ عند النقطة $(2, 5)$ الواقعة عليه موازياً للمحور $x$.
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>54  الفصل 2 تطبيقات المشتقة</b>
</div>
<!-- PAGE_END_54 -->


<!-- PAGE_START_55 -->
### صفحة 55

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>13</b> أوجد معادلتي المماس والعمودي للمنحنى $y = x^3 - 2x^2 + 4$ عند النقطة $(2, 4)$ الواقعة عليه.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>14</b> أوجد معادلتي المماس والعمودي للمنحنى $x^2 - y^2 = 7$ عند النقطة $(4, -3)$ الواقعة عليه.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>15</b> أوجد معادلتي المماس والعمودي للمنحنى $y = \frac{5}{x^2 + 1}$ عند النقطة $(-2, 1)$ الواقعة عليه.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>16</b> أوجد معادلات كل من المماس والعمودي للمنحنى $y = x^3 - 5x$ عند نقطة تقاطعه مع المستقيم $y = 4x$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>17</b> أوجد معادلتي المماس والعمودي للمنحنى $y^2 - x^2 = 12$ عند النقطة $(4, -2)$ الواقعة عليه.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>18</b> أوجد النقاط الواقعة على منحنى $y = 4x^3 - 21x^2 + 30x$ ، والتي يكون المماس عندها موازياً للمحور $x$ ، ثم أوجد معادلة العمودي على المنحنى عند كل نقطة.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>19</b> أوجد قيمتي $a , b$ ، إذا كان منحنى $y = ax^3 + bx^2$ يمس المستقيم $3x + y - 1 = 0$ عند النقطة $(1, -2)$ ، ثم أوجد معادلة العمودي على المنحنى عند النقطة نفسها.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>20</b> أوجد معادلتي المماس والعمودي للمنحنى $2x^2 + 2y^2 - 5x + 3y + 1 = 0$ عند النقطة $(1, -2)$ الواقعة عليه.
</div>

<br>

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>الدرس 1-2 تطبيقات هندسية</b> | <b>55</b>
</div>
<!-- PAGE_END_55 -->


<!-- PAGE_START_56 -->
### صفحة 56

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>2-2 تطبيقات فيزيائية</h2>
<p><strong>Physical Applications</strong></p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
كما أن للمشتقة تطبيقات هندسية، فإن لها أيضًا تطبيقات فيزيائية تمكننا من إيجاد السرعة إذا علمت العلاقة بين الإزاحة (المسافة) والزمن، وإيجاد التسارع إذا علمت العلاقة بين السرعة والزمن لجسم يتحرك في خط مستقيم.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: #c00000; margin-bottom: 5px;">السرعة والتسارع ( العجلة )</h3>
نفترض أن جسيمًا يتحرك في خط مستقيم مبتدئًا من النقطة الثابتة $O$ كما في الشكل المجاور، وبعد فترة زمنية مقدارها $t$ أصبح الجسيم عند النقطة $p$ حيث ($Op = s$)، وإذا أصبح موضعه عند $p'$ بعد فترة زمنية أخرى مقدارها $\Delta t$، حيث ($pp' = \Delta s$)؛ بمعنى أن كل تغير في الزمن $t$ يناظره تغير في الإزاحة $s$، فإن:
</div>

$$s = f(t)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: #c00000; margin-bottom: 5px;">السرعة المتوسطة</h3>
حيث إن السرعة المتوسطة هي خارج قسمة التغير في الإزاحة $s$ على التغير المناظر في الزمن $t$، وإذا رمزنا للسرعة المتوسطة بالرمز $v_{avg}$ ، فإن:
</div>

$$v_{avg} = \frac{\Delta s}{\Delta t}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: #c00000; margin-bottom: 5px;">السرعة اللحظية</h3>
حيث إن السرعة اللحظية لجسيم متحرك هي السرعة المتوسطة لهذا الجسيم خلال فترة زمنية صغيرة جدًا تؤول إلى الصفر، وإذا رمزنا للسرعة اللحظية بالرمز $v$ ، فإن:
</div>

$$v = \lim_{\Delta t \to 0} \frac{\Delta s}{\Delta t}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن السرعة اللحظية $v$ لجسيم متحرك عند لحظة ما هي المشتقة الأولى للإزاحة $s$ بالنسبة للزمن عند تلك اللحظة.
</div>

$$v = \frac{ds}{dt} = f'(t)$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>56</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>الفصل 2 تطبيقات المشتقة</strong>
</div>
<!-- PAGE_END_56 -->


<!-- PAGE_START_57 -->
### صفحة 57

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 1</b><br>
تتحرك نقطة مادية في خط مستقيم، إذا كانت العلاقة بين الإزاحة $s$ بالسنتيمترات عن نقطة ثابتة $O$، والزمن $t$ بالثواني هي $s = t^3 - 9t^2 + 24t$، فأوجد سرعة هذه النقطة بعد مرور $5\text{ sec}$ من بدء الحركة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
</div>

$$\because s = t^3 - 9t^2 + 24t$$

$$v = \frac{ds}{dt}$$

$$\therefore v = 3t^2 - 18t + 24$$

$$\therefore v_{t=5\text{sec}} = 3(5)^2 - 18(5) + 24$$

$$= 9\text{ cm/sec}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 2</b><br>
يتحرك جسم في خط مستقيم، إذا كانت العلاقة بين الإزاحة $s$ بالأمتار عن نقطة ثابتة، والزمن $t$ بالدقائق هي $s = 5t + 7$، فأوجد سرعة هذا الجسم.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
</div>

$$\because s = 5t + 7 \quad , \quad v = \frac{ds}{dt}$$

$$\therefore v = 5\text{ m/min}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن الجسم يتحرك بسرعة منتظمة.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b style="color: #c00000;">متوسط التسارع</b><br>
إذا كانت السرعة اللحظية لجسيم متحرك في خط مستقيم عند لحظة ما $t$ هي $v$، وبعد فترة زمنية مقدارها $(\Delta t)$ أصبحت سرعته $(v + \Delta v)$، فإن خارج قسمة التغير في السرعة على التغير المناظر في الزمن يسمى متوسط التسارع. وإذا رمزنا لمتوسط التسارع بالرمز $a_{avg}$، فإن متوسط التسارع للجسيم خلال هذه الفترة الزمنية $(\Delta t)$ هي:
</div>

$$a_{avg} = \frac{\Delta v}{\Delta t}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b style="color: #c00000;">التسارع اللحظي</b><br>
حيث إن التسارع اللحظي لجسيم متحرك هو متوسط التسارع لهذا الجسيم خلال فترة زمنية صغيرة جداً تؤول إلى الصفر، وإذا رمزنا للتسارع اللحظي بالرمز $a$، فإن:
</div>

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>الدرس 2-2</b> تطبيقات فيزيائية | <b>57</b>
</div>
<!-- PAGE_END_57 -->


<!-- PAGE_START_58 -->
### صفحة 58

$$a = \lim_{\Delta t \to 0} a_{\text{avg}} = \lim_{\Delta t \to 0} \frac{\Delta v}{\Delta t} = \frac{dv}{dt} = \frac{d}{dt}\left(\frac{ds}{dt}\right) = \frac{d^2s}{dt^2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن التسارع اللحظي هو المشتقة الأولى للسرعة بالنسبة للزمن، وهو أيضًا المشتقة الثانية للمسافة بالنسبة للزمن.
</div>

$$a = \frac{dv}{dt} = \frac{d^2s}{dt^2}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>ملاحظات:</strong>
<ul>
<li>كل من الإزاحة والسرعة والتسارع كمية متجهة.</li>
<li>إذا عاد الجسم المتحرك إلى نقطة البداية، فإن إزاحته تكون مساوية للصفر.</li>
<li>إذا غير الجسم المتحرك - في خط مستقيم - اتجاه حركة في لحظة ما، فإن سرعته عند هذه اللحظة تكون مساوية للصفر.</li>
<li>إذا انعدم تسارع الجسم المتحرك في خط مستقيم ($a = 0$)، فإن الجسم إما أن يكون ساكنًا، أو متحركًا بسرعة منتظمة.</li>
<li>إذا كان تسارع جسم متحرك في فترة زمنية ما موجباً، فإن سرعة الجسم في هذه الفترة تكون في تزايد.</li>
<li>إذا كان تسارع جسم متحرك في فترة زمنية ما سالباً، فإن سرعة الجسم في هذه الفترة تكون في تناقص.</li>
</ul>
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3:</strong>
<br>
يتحرك جسم في خط مستقيم، بحيث كانت العلاقة بين الإزاحة $s$ بالسنتيمترات، والزمن $t$ بالثواني هي $s = 4 \sin 2t$ ، أوجد سرعته، وتسارعه عندما $t = \frac{\pi}{6} \text{ sec}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because s = 4 \sin 2t , \quad v = \frac{ds}{dt}$$

$$\therefore v = 8 \cos 2t$$

$$(v)_{t = \frac{\pi}{6}\text{ sec}} = 8 \cos \frac{\pi}{3}$$

$$= 4 \text{ cm/sec}$$

$$\because v = 8 \cos 2t , \quad a = \frac{dv}{dt}$$

$$\therefore a = -16 \sin 2t$$

$$= a_{t = \frac{\pi}{6}\text{ sec}} = -16 \sin \frac{\pi}{3}$$

$$= -8 \sqrt{3} \text{ cm/sec}^2$$

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>الفصل 2 تطبيقات المشتقة</strong>
</div>
<!-- PAGE_END_58 -->


<!-- PAGE_START_59 -->
### صفحة 59

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4</strong>
<br>
تحرك جسم في خط مستقيم، بحيث كانت العلاقة بين الإزاحة $s$ بالسنتيمترات، والزمن $t$ بالثواني هي $s = t^3 - 3t^2 + 5t + 4$، أوجد كلاً من المسافة التي يقطعها الجسم، وسرعته عندما ينعدم التسارع.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because s = t^3 - 3t^2 + 5t + 4 \quad , \quad v = \frac{ds}{dt}$$

$$\therefore v = 3t^2 - 6t + 5 \quad , \quad a = \frac{dv}{dt}$$

$$\therefore a = 6t - 6$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عندما ينعدم التسارع، فإن:
</div>

$$6t - 6 = 0 \rightarrow t = 1 \text{ sec}$$

$$(s)_{t = 1 \text{ sec}} = (1)^3 - 3(1)^2 + 5(1) + 4$$
$$= 7 \text{ cm}$$

$$(v)_{t = 1 \text{ sec}} = 3(1)^2 - 6(1) + 5$$
$$= 2 \text{ cm/sec}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5</strong>
<br>
إذا كانت العلاقة بين الإزاحة $s$ بالسنتيمترات، والزمن $t$ بالثواني لجسم متحرك في خط مستقيم هي $s = 12t^2 - t^3$، فأجب عما يأتي:
<br>
<strong>a)</strong> متى يعكس الجسم اتجاه حركته، وأين؟
<br>
<strong>b)</strong> متى يصل الجسم إلى نقطة البداية؟
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
<br>
<strong>(a</strong>
</div>

$$\because s = 12t^2 - t^3 \quad , \quad v = \frac{ds}{dt}$$

$$\therefore v = 24t - 3t^2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ الجسم يعكس اتجاه حركته عندما $v = 0$
</div>

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 2-2 تطبيقات فيزيائية | 59
</div>
<!-- PAGE_END_59 -->


<!-- PAGE_START_60 -->
### صفحة 60

<div dir="rtl" style="text-align: right; font-size: 16px;">

$$\therefore 24 t - 3 t^2 = 0$$
$$3 t (8 - t) = 0$$
$$t = 0 \text{ (عند بدء الحركة) أو } t = 8\text{ sec}$$
$$\therefore \text{يعكس الجسم اتجاه حركته بعد مرور } 8\text{ sec} \text{ من بدء الحركة، ويكون:}$$
$$(s)_{t = 8\text{ sec}} = 12 (8)^2 - (8)^3$$
$$= 256\text{ cm}$$
$$\therefore \text{يعكس الجسم اتجاه حركته بعد قطع مسافة } 256\text{ cm} .$$

<strong>b)</strong> يصل الجسم إلى نقطة البداية عندما $s = 0$
<br>
أي أن:
$$12 t^2 - t^3 = 0$$
$$t^2 (12 - t) = 0$$
$$t = 0 \text{ (عند بدء الحركة) أو } t = 12\text{ sec}$$
$$\therefore \text{يصل الجسم إلى نقطة البداية بعد مرور زمن قدره } 12\text{ sec} \text{ من بدء الحركة.}$$

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">

<strong>مثال 6:</strong>
<br>
أُطلق بالون لمراقبة الطقس ليرتفع رأسياً، وكانت العلاقة بين المسافة $s$ بالأمتار التي يرتفعها البالون، والزمن $t$ بالثواني خلال العشر ثوان الأولى للحركة هي $s = 2 + \frac{t}{2} + \frac{t^2}{4}$.

أجب عما يأتي:
<br>
<strong>a)</strong> أوجد سرعة البالون بعد مرور زمن قدره $7\text{ sec}$ من لحظة بدء الحركة.
<br>
<strong>b)</strong> احسب سرعة البالون بعد قطع $8\text{ m}$ من لحظة انطلاقه.

<br>
<strong>الحل</strong>
<br>
<strong>a)</strong>
$$\because s = 2 + \frac{t}{2} + \frac{t^2}{4} \quad , \quad v = \frac{ds}{dt}$$
$$\therefore v = \frac{1}{2} + \frac{t}{2}$$

</div>

<div dir="rtl" style="text-align: right; font-size: 14px;">
60 | الفصل 2: تطبيقات المشتقة
</div>
<!-- PAGE_END_60 -->


<!-- PAGE_START_61 -->
### صفحة 61

$$(v)_{t=7\text{ sec}} = \frac{1}{2} + \frac{7}{2}$$
$$= 4\text{ m/sec}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>b)</b>
</div>

$$\because s = 2 + \frac{t}{2} + \frac{t^2}{4} \quad , \quad s = 8\text{ m}$$
$$\therefore 8 = 2 + \frac{t}{2} + \frac{t^2}{4}$$
$$t^2 + 2t - 24 = 0$$
$$(t + 6)(t - 4) = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$t = 4\text{ sec}$ أو $t = -6$ (مرفوض)
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ يكون البالون على ارتفاع $8\text{ m}$ بعد زمن قدره $4\text{ sec}$ من لحظة بدء الانطلاق،
</div>

$$(v)_{t=4\text{ sec}} = \frac{1}{2} + \frac{4}{2} = 2.5\text{ m/sec}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 7</b>
<br>
قُذف جسم رأسياً إلى أعلى، وكانت العلاقة بين ارتفاعه $s$ بالأمتار عن سطح الأرض، والزمن $t$ بالثواني هي $s = 96t - 16t^2$. أوجد كلاً مما يأتي:
<br>
<b>a)</b> زمن وصول الجسم إلى أقصى ارتفاع.
<br>
<b>b)</b> مجموعة قيم $t$ التي تكون السرعة عندها أكبر من الصفر (حيث $t \ge 0$).
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
<br>
<b>a)</b>
</div>

$$\because s = 96t - 16t^2 \quad , \quad v = \frac{ds}{dt}$$
$$\therefore v = 96 - 32t$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عند أقصى ارتفاع تكون $v = 0$
</div>

$$\therefore 96 - 32t = 0 \Rightarrow t = 3\text{ sec}$$

---
<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 2-2 تطبيقات فيزيائية | 61
</div>
<!-- PAGE_END_61 -->


<!-- PAGE_START_62 -->
### صفحة 62

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن الجسم يصل إلى أقصى ارتفاع بعد مرور زمن قدره $3\text{ sec}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(b</b>
</div>

$$\because v > 0$$
$$\because 96 - 32t > 0$$
$$32t < 96$$
$$\therefore t < 3 \quad , \quad t \ge 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ مجموعة قيم $t$ التي تكون عندها السرعة أكبر من الصفر هي $(0, 3]$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 8</b>
<br>
يتحرك جسم في خط مستقيم وفقاً للعلاقة $s = f(t) = \frac{1}{3}t^3 - 2t^2 + 3t$، حيث الإزاحة $s$ تقاس بالأمتار ($\text{m}$)، والزمن $t$ بالثواني ($\text{sec}$). أوجد التسارع $a$ عندما تكون السرعة $v$ مساوية للصفر.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
<br>
لإيجاد السرعة $v$ نوجد مشتقة $f(t)$.
</div>

$$\because s = f(t) = \frac{1}{3}t^3 - 2t^2 + 3t$$
$$\therefore v = \frac{ds}{dt} = f'(t) = t^2 - 4t + 3$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ التسارع هي المشتقة الأولى للسرعة بالنسبة للزمن، وهي أيضاً المشتقة الثانية للمسافة بالنسبة للزمن.
</div>

$$\therefore a = \frac{dv}{dt} = f''(t) = 2t - 4$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عندما تكون السرعة مساوية للصفر ($v = 0$)
</div>

$$\therefore t^2 - 4t + 3 = 0$$
$$(t - 3)(t - 1) = 0$$
$$t - 3 = 0 \Rightarrow t = 3\text{ sec}$$
$$t - 1 = 0 \Rightarrow t = 1\text{ sec} \quad \text{أو}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أن $v = 0$ بعد مرور $1\text{ sec}$، أو $3\text{ sec}$ من بدء الحركة.
<br>
لذا، فإن:
</div>

$$a(1) = 2(1) - 4 = -2\text{ m/sec}^2$$
$$a(3) = 2(3) - 4 = 2\text{ m/sec}^2$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>62</b> الفصل 2 تطبيقات المشتقة
</div>
<!-- PAGE_END_62 -->


<!-- PAGE_START_63 -->
### صفحة 63

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين 2-2</h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد السرعة والتسارع (العجلة) في كل مما يأتي، حيث الإزاحة $s$ بالأمتار، والزمن $t$ بالثواني:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>1)</b> $$s = t^2 - 3t \, , \quad t = \frac{5}{2} \text{ sec}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>2)</b> $$s = 3t^2 - 12t + 1 \, , \quad t = 2 \text{ sec}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>3)</b> $$s = 24 + 6t - t^3 \, , \quad t = 3 \text{ sec}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>4)</b> $$s = 2t^4 - 3t^3 \, , \quad t = 0.5 \text{ sec}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>5)</b> $$s = 2t^3 - \frac{5}{t} \, , \quad t = 1 \text{ sec}$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>6)</b> إذا كانت العلاقة بين المسافة $s$ بالأمتار، والزمن $t$ بالثواني هي $s = t^3 - 12t^2 + 36t$ ، فأوجد كلاً مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-right: 20px;">
<b>a)</b> السرعة والتسارع عند أي لحظة.<br>
<b>b)</b> الإزاحة والتسارع في حالة السكون اللحظي.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>7)</b> قُذف جسم رأسيًا إلى أعلى، إذا كان ارتفاع الجسيم $s$ بالأمتار بعد زمن مقداره $t$ ثانية من لحظة قذفه يعطى بالعلاقة $s = 112t - 16t^2$ . أوجد كلاً مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-right: 20px;">
<b>a)</b> سرعة الجسم وتسارعه بعد مرور $3 \text{ sec}$ من لحظة القذف.<br>
<b>b)</b> أقصى ارتفاع يصل إليه الجسم ابتداء من نقطة القذف.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>8)</b> إذا كانت إزاحة نقطة مادية عن نقطة ثابتة تتحرك في خط مستقيم عند لحظة ما وفقًا للعلاقة $s = t^3 - 6t^2 + 9t$ ، فأوجد تسارع الحركة عندما يتغير اتجاه حركة النقطة المادية، علمًا أن المسافة بالأمتار والزمن بالدقائق.
</div>

<br><br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>63</b> &nbsp;&nbsp;&nbsp;&nbsp; الدرس 2-2 تطبيقات فيزيائية
</div>
<!-- PAGE_END_63 -->


<!-- PAGE_START_64 -->
### صفحة 64

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>9</b> يتحرك جسم في خط مستقيم وفقًا للعلاقة $s = (t - 2)^2 (2t - 1)$ ، حيث الإزاحة $s$ بالسنتيمترات ، الزمن $t$ بالثواني ، فأوجد كلاً مما يأتي :
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>a)</b> السرعة الابتدائية للجسم .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>b)</b> الفترة الزمنية التي يتحرك فيها الجسم بسرعة $v$ (حيث $v > 0$) .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>10</b> يتحرك جسم رأسيًا إلى أعلى ابتداء من نقطة على سطح الأرض وفقًا للعلاقة $s = 64t - 16t^2$ ، أوجد سرعة الجسم عندما يكون على ارتفاع $48\text{ m}$ عن سطح الأرض (نقطة البداية)، علمًا أن الزمن بالثواني .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>11</b> يتحرك جسم في خط مستقيم، إذا كانت العلاقة بين الإزاحة $s$ بالكيلومترات ($\text{km}$) ، والزمن $t$ بالساعات ($\text{h}$) هي $s = 120 + 20t - t^2$ . أوجد كلاً مما يأتي :
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>a)</b> السرعة $v$ والتسارع ($a$) بعد $5\text{ h}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>b)</b> الإزاحة $s$ عندما $v = 0$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>12</b> يتحرك جسم في خط مستقيم وفقًا للعلاقة $s = 2 \cos^2 t$ ، حيث الإزاحة $s$ بالسنتيمترات ($\text{cm}$)، والزمن $t$ بالثواني ($\text{sec}$). أوجد تسارع الجسم $a$ بعد مضي زمن قدره $t = \frac{\pi}{2}\text{ sec}$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>13</b> يتحرك جسم في خط مستقيم، وإزاحته $s$ بالأمتار ($\text{m}$) بعد $t$ ثانية عن نقطة ثابتة تعطى بالعلاقة $s = 4 \cos 3t + 4 \sin 3t$ ، أجب عما يأتي :
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>a)</b> أثبت أن $a = -9s$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>b)</b> أوجد التسارع $a$ بعد مرور $\frac{\pi}{3}\text{ sec} \,,\, \frac{\pi}{6}\text{ sec}$ .
</div>

<br><br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>64</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>الفصل 2</b> تطبيقات المشتقة
</div>
<!-- PAGE_END_64 -->


<!-- PAGE_START_65 -->
### صفحة 65

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1><b>2-3 المعدلات الزمنية المرتبطة</b></h1>
<p><b>The Related Rates</b></p>

من التطبيقات المهمة لقاعدة التسلسل، والاشتقاق بصورة عامة ما يسمى <b>بالمعدلات الزمنية المرتبطة</b>، حيث تستعمل فكرة الاشتقاق للدوال المرتبطة بالزمن.
<br>
فمثلاً، إذا كانت المتغيرات $x, y, z$ مرتبطة بالزمن، والعلاقة بينهم هي:
</div>

$$x^3 + 4y^2 - 8z = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فإنه بالاشتقاق بالنسبة للزمن $t$ نحصل على:
</div>

$$3x^2 \frac{dx}{dt} + 8y \frac{dy}{dt} - 8 \frac{dz}{dt} = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويمكن إيجاد أحد هذه المعدّلات، إذا علمت المعدّلات الأخرى عند قيم محدّدة لهذه المتغيرات. والأمثلة الآتية توضح ذلك.
<br><br>
ويَدُلُّ معدّل التغيُّر الموجب على ازدياد قيمة المتغير مع مرور الزمن، فيما يدُلُّ معدّل التغيُّر السالب على تناقص قيمة المتغير مع مرور الزمن.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<table border="0" style="width: 100%;">
<tr>
<td style="vertical-align: top;">
<b style="background-color: #2b5b84; color: white; padding: 5px 10px; border-radius: 5px;">مثال 1</b>
<br><br>
يتمدد مربع من المعدن بالحرارة بانتظام. إذا كان معدّل تغيُّر طول ضلعه $0.03\text{ cm/sec}$، فأوجد معدّل التغيُّر في مساحة سطحه عندما يكون طول ضلعه مساوياً $10\text{ cm}$.
<br><br>
<b style="color: #b83227;">الحل</b>
<br>
افرض أن طول ضلع المربع هو $L$ بالسنتيمترات، ومساحة سطحه $A$ بالسنتيمترات المربعة ،
</td>
</tr>
</table>
</div>

$$\because A = L^2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$\therefore \frac{dA}{dt} = 2L \frac{dL}{dt} \quad , \quad L = 10\text{ cm} \quad , \quad \frac{dL}{dt} = 0.03\text{ cm/sec}$$

$$\therefore \frac{dA}{dt} = 2 (10) (0.03)$$

$$= 0.6\text{ cm}^2/\text{sec}$$

<br>
<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>65</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;الدرس 3-2 المعدلات الزمنية المرتبطة
</div>
<!-- PAGE_END_65 -->

<!-- PAGE_START_66 -->
### صفحة 66

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 2</strong><br>
أُلقي حجر في مياه بحيرة ساكنة، فأحدث موجات دائرية تتزايد أنصاف أقطارها بمعدّل ثابت مقداره $0.5 \text{ m/sec}$. ما مقدار معدّل التغيّر في محيط إحدى هذه الموجات، عندما كان نصف قطرها $4 \text{ m}$؟
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
افرض أن طول نصف قطر إحدى هذه الموجات $r$ بالأمتار، ومحيط هذه الموجة الدائرية هو $p$ بالأمتار.
</div>

$$ \because p = 2 \pi r $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$ \therefore \frac{dp}{dt} = 2 \pi \frac{dr}{dt} , \quad \frac{dr}{dt} = 0.5 \text{ m/sec} $$

$$ \therefore \frac{dp}{dt} = 2 \pi (0.5) $$

$$ = \pi \text{ m/sec} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3</strong><br>
سُخِّنت صفحة معدنية دائرية الشكل، وكان معدّل زيادة نصف قطرها يساوي $0.005 \text{ cm/min}$. أوجد معدّل زيادة مساحة سطح الصفحة، عندما يكون طول نصف قطرها $15 \text{ cm}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
افرض أن طول نصف قطر الصفحة هو $r$ بالسنتيمترات، ومساحة سطحها هو $A$ بالسنتيمترات المربعة،
</div>

$$ \because A = \pi r^2 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$ \therefore \frac{dA}{dt} = 2 \pi r \frac{dr}{dt} , \quad r = 15 \text{ cm} , \quad \frac{dr}{dt} = 0.005 \text{ cm/min} $$

$$ \therefore \frac{dA}{dt} = 2 \pi (15) (0.005) $$

$$ = 0.15 \pi \text{ cm}^2 /\text{min} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 2 تطبيقات المشتقة | 66
</div>
<!-- PAGE_END_66 -->



<!-- PAGE_START_67 -->
### صفحة 67

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
تتحرك نقطة على منحنى $y = x^2 + 2$ ، وفي لحظة ما كان $\frac{dx}{dt} = 0.25$ ، $\frac{dy}{dt} = 0.3\text{ cm/sec}$ . أوجد موضع النقطة على المنحنى عند تلك اللحظة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because y = x^2 + 2 \text{ .................(1)}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$\frac{dy}{dt} = 2x \frac{dx}{dt} , \quad \frac{dx}{dt} = 0.25\text{ cm/sec} , \quad \frac{dy}{dt} = 0.3\text{ cm/sec}$$

$$\therefore 0.3 = 2x (0.25)$$

$$x = \frac{0.3}{0.5} = 0.6$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالتعويض عن قيمة $x$ في المعادلة (1) ينتج أن:
</div>

$$y = (0.6)^2 + 2$$

$$= 2.36$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ موضع النقطة على المنحنى عند تلك اللحظة هو $(0.6 , 2.36)$ .
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
يتسرب غاز من بالون كروي بمعدل $600\text{ cm}^3/\text{sec}$ . أوجد معدل تغيّر طول نصف قطر البالون، ومعدل تغيّر مساحة سطحه عندما يكون طول نصف القطر $300\text{ cm}$ ، علماً أن حجم الكرة هو $v = \frac{4}{3} \pi r^3$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
افرض أن طول نصف قطر البالون الكروي هو $r$ بالسنتيمترات ، وحجمه هو $v$ بالسنتيمترات المكعبة، ومساحة سطحه هو $A$ بالسنتيمترات المربعة،
</div>

$$\because v = \frac{4}{3} \pi r^3$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$\therefore \frac{dv}{dt} = \frac{4}{3} \pi (3 r^2) \frac{dr}{dt}$$

$$= 4 \pi r^2 \frac{dr}{dt}$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
67 | الدرس 3-2 المعدلات الزمنية المرتبطة
</div>
<!-- PAGE_END_67 -->


<!-- PAGE_START_68 -->
### صفحة 68

<div dir="rtl" style="text-align: right; font-size: 16px;">
وحيث إن الغاز يتسرب بمعدل $600\text{ cm}^3/\text{sec}$
</div>

$$ \therefore \frac{dv}{dt} = -600\text{ cm}^3/\text{sec} \text{ , } r = 300\text{ cm} $$

$$ \therefore -600 = 4\pi (300)^2 \frac{dr}{dt} $$

$$ \therefore \frac{dr}{dt} = -\frac{1}{600\pi}\text{ cm}/\text{sec} $$

$$ \because A = 4\pi r^2 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$ \therefore \frac{dA}{dt} = 4\pi (2r) \frac{dr}{dt} \text{ , } r = 300\text{ cm} \text{ , } \frac{dr}{dt} = -\frac{1}{600\pi}\text{ cm}/\text{sec} $$

$$ = 4\pi (2(300)) \left( -\frac{1}{600\pi} \right) $$

$$ = -4\text{ cm}^2/\text{sec} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 6:</strong><br>
حوض على شكل متوازي مستطيلات طول قاعدته $200\text{ cm}$ ، وعرضها $50\text{ cm}$ ، عمقه $100\text{ cm}$ ، إذا كان الماء ينساب داخله بمعدل $900\text{ cm}^3/\text{sec}$ ، فأحسب معدل ارتفاع منسوب الماء في الحوض.<br>
(علماً بأن حجم متوازي المستطيلات = الطول $\times$ العرض $\times$ الارتفاع)
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
افرض أن حجم الماء في الحوض هو $v$ بالسنتيمترات المكعبة ، وارتفاعه عند اللحظة $t\text{ sec}$ هو $z$ بالسنتيمترات،
</div>

$$ \therefore v = (50) (200) (z) = 10000z $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$ \therefore \frac{dv}{dt} = 10000 \frac{dz}{dt} \text{ , } \frac{dv}{dt} = 900\text{ cm}^3/\text{sec} $$

$$ \therefore 900 = 10000 \frac{dz}{dt} $$

$$ \therefore \frac{dz}{dt} = 0.09\text{ cm}/\text{sec} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 2 تطبيقات المشتقة
</div>
<!-- PAGE_END_68 -->


<!-- PAGE_START_69 -->
### صفحة 69

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 7</b><br>
سُخن قضيب معدني دائري المقطع، فازداد طوله بمعدل $0.005\text{ cm/min}$. وفي الوقت نفسه ازداد طول نصف قطر مقطعه بمعدل $0.001\text{ cm/min}$، أوجد معدل زيادة حجم القضيب، عندما يكون طوله $40\text{ cm}$، وطول نصف قطر مقطعه $2\text{ cm}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b><br>
افرض أن طول القضيب هو $L$ بالسنتيمترات، وطول نصف قطر مقطعه هو $r$ بالسنتيمترات، وحجمه هو $v$ بالسنتيمترات المكعبة،
</div>

$$\because v = \pi r^2 L$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$\therefore \frac{dv}{dt} = \pi \left[ r^2 \frac{dL}{dt} + L(2r) \frac{dr}{dt} \right]$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because \frac{dL}{dt} = 0.005\text{ cm/min}, \quad \frac{dr}{dt} = 0.001\text{ cm/min}, \quad L = 40\text{ cm}, \quad r = 2\text{ cm}$
</div>

$$\therefore \frac{dv}{dt} = \pi \left[ (2)^2 (0.005) + 40 (4) (0.001) \right]$$

$$= 0.18\pi \text{ cm}^3/\text{min}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 8</b><br>
يستند سلم طوله $5\text{ m}$ على حائط رأسي. إذا كان الطرف السفلي للسلم ينزلق أفقياً مبتعداً عن الحائط بمعدل $0.5\text{ m/sec}$، فأوجد معدل انزلاق الطرف العلوي للسلم على الحائط، عندما يكون الطرف السفلي له على بُعد $3\text{ m}$ من الحائط.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b><br>
افرض أن الطرف السفلي للسلم يبعد عن الحائط بُعداً قدره $x$ بالأمتار، وارتفاع الطرف العلوي للسلم عن الأرض هو $y$ بالأمتار، فتكون العلاقة بين $x , y$ هي:
</div>

$$\because x^2 + y^2 = 25$$

$$\therefore (3)^2 + y^2 = 25$$

$$y^2 = 25 - 9$$

$$\therefore y = 4\text{ m}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالاشتقاق بالنسبة للزمن $t$
</div>

$$\therefore 2x \frac{dx}{dt} + 2y \frac{dy}{dt} = 0 , \quad \because \frac{dx}{dt} = 0.5\text{ m/sec}$$

$$\therefore 2 (3) (0.5) + 2(4) \frac{dy}{dt} = 0 \Rightarrow \frac{dy}{dt} = -\frac{3}{8}\text{ m/sec}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ معدل انزلاق الطرف العلوي للسلم على الحائط يساوي $\frac{3}{8}\text{ m/sec}$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 3-2 المعدلات الزمنية المرتبطة &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>69</b>
</div>
<!-- PAGE_END_69 -->


<!-- PAGE_START_70 -->
### صفحة 70

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين 2-3</h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
1. تتحرك نقطة مادية على المنحنى $y - x^2 = 6$ ، وعند لحظة ما كان $\frac{dx}{dt} = 0.1\text{ cm/sec}$ ، $\frac{dy}{dt} = 0.2\text{ cm/sec}$ ، أوجد موضع النقطة عند تلك اللحظة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2. قرص معدني ينكمش بالتبريد، حيث ينقص قطره بمعدل $0.04\text{ cm/min}$ . أوجد معدل النقص في مساحة سطح القرص عندما يكون طول نصف قطره $20\text{ cm}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3. مكعب يتمدد بالحرارة، فيزداد طول حرفه بمعدل $0.001\text{ cm/sec}$ . أوجد معدل زيادة حجمه عندما يكون طول حرفه $40\text{ cm}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
4. يتسرب غاز من بالون كروي بمعدل $0.3\text{ m}^3/\text{h}$ . أوجد معدل التغير في طول نصف قطره عندما يكون طول نصف قطر البالون $2\text{ m}$ .
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
5. خزان ماء على شكل مخروط دائري قائم، رأسه إلى أسفل، ارتفاعه $2\text{ m}$ ، طول نصف قطر قاعدته $1\text{ m}$ . إذا ضُخَّ الماء في الخزان بمعدل $0.04\text{ m}^3/\text{min}$ ، فأوجد معدل ارتفاع الماء في الخزان عندما يكون ارتفاع الماء فيه $0.5\text{ m}$ (علماً أن حجم المخروط = $\frac{1}{3}$ مساحة القاعدة $\times$ الارتفاع).
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
6. خزان للمياه على شكل متوازي مستطيلات بعدا قاعدته $4\text{ m} , 6\text{ m}$ . إذا تسرب الماء منه بمعدل $0.48\text{ m}^3/\text{min}$ ، فأوجد معدل انخفاض سطح الماء فيه.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
7. حوض على شكل مكعب طول ضلعه $2\text{ m}$ ، يُصَبُّ فيه الماء بمعدل $0.24\text{ m}^3/\text{min}$ . أوجد معدل ارتفاع الماء في الحوض.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
8. سلم طوله $8.5\text{ m}$ يرتكز بطرفه الأعلى على حائط رأسي، وبطرفه الأسفل على أرض أفقية. إذا كان الطرف الأعلى يهبط رأسياً إلى أسفل بمعدل $5\text{ m/sec}$ ، فاحسب سرعة ابتعاد الطرف الأسفل عن الحائط، عندما يكون هذا الطرف على بُعد $7.5\text{ m}$ من الحائط.
</div>
<!-- PAGE_END_70 -->


<!-- PAGE_START_71 -->
### صفحة 71

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>2-4 تطبيقات المشتقة الأولى والثانية</h2>
<p><strong>Applications of the first and second derivative</strong></p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
لحساب التفاضل تطبيقات متعددة، وقد درست بعضاً منها (ميل المماس، السرعة اللحظية، العجلة)، وسنتناول في هذا الدرس استعمالات أخرى لهذا الموضوع، وأهمها كيفية رسم بعض الدوال.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>تزايد الدوال وتناقصها</h3>
سبق وأن تعرفت على الدوال المطردة (المتزايدة والمتناقصة)، وفيما يأتي سنرى كيف أن إشارة المشتقة الأولى لدالة ما في مجال تعريفها تكون ذات دلالة معينة بالنسبة لتزايد، أو تناقص (اطراد) الدالة.
</div>

<hr />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>إرشادات للدراسة</strong>

<strong>الاتصال في الفترات</strong>
<ul>
  <li>إذا كانت الدالة $f(x)$ معرفة على $[a, b]$، فإنها تكون متصلة في $(a, b)$، إذا وفقط إذا كانت الدالة $f(x)$ متصلة $\forall x \in (a, b)$.</li>
  <li>تكون الدالة $f(x)$ متصلة في $[a, b]$، إذا وفقط إذا كانت:
    <ol>
      <li>$f(x)$ متصلة في $(a, b)$.</li>
      <li>$f(x)$ متصلة على يمين $x = a$؛ أي أن $\lim_{x \to a^+} f(x) = f(a)$</li>
      <li>$f(x)$ متصلة على يسار $x = b$؛ أي أن $\lim_{x \to b^-} f(x) = f(a)$</li>
    </ol>
  </li>
</ul>

<strong>قابلية الاشتقاق</strong><br />
إذا وجدت للدالة $f(x)$ مشتقة عند كل $x \in (a, b)$، فإن هذا يعني أن الدالة $f(x)$ قابلة للاشتقاق في هذه الفترة، وإذا كانت الدالة $f(x)$ قابلة للاشتقاق عند كل $x \in \mathbb{R}$، فإن هذا يعني أن الدالة $f(x)$ قابلة للاشتقاق في $\mathbb{R}$.
</div>

<hr />

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدالة الممثلة بيانياً في كل شكل أعلاه دالة متناقصة، ونلاحظ من تمثيلها البياني أن الزاوية $\theta$ التي يصنعها المماس عند أي نقطة على منحنى الدالة (ما عدا طرفيها) مع الاتجاه الموجب للمحور $x$ منفرجة، وبالتالي، فإن $\tan\theta < 0 \Rightarrow f'(x) < 0$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبصفة عامة إذا كانت الدالة $f(x)$ متصلة في $[a, b]$، وقابلة للاشتقاق في $(a, b)$، وكانت:
</div>

$$f'(x) < 0 \quad \forall x \in (a, b)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
فإن الدالة $f(x)$ تكون متناقصة في $[a, b]$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
والدالة الممثلة بيانياً في كل شكل أعلاه دالة متزايدة، وهنا نرى أن الزاوية $\theta$ التي يصنعها المماس عند أي نقطة على منحنى الدالة (ما عدا طرفيها) مع الاتجاه الموجب للمحور $x$ حادة وبالتالي، فإن $\tan\theta > 0 \Rightarrow f'(x) > 0$.
</div>

<br />

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية | 71
</div>
<!-- PAGE_END_71 -->


<!-- PAGE_START_72 -->
### صفحة 72

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبصفة عامة إذا كانت الدالة $f(x)$ متصلة في $[a, b]$ ، وقابلة للاشتقاق في $(a, b)$ ، وكانت
$$f'(x) < 0 \quad \forall x \in (a, b)$$
فإن الدالة $f(x)$ تكون متزايدة في $[a, b]$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>بدون برهان</strong>

**نظرية**

لتكن الدالة $f$ متصلة في $[a, b]$ ، وقابلة للاشتقاق في $(a, b)$ ، إذا كانت:

1) $f'(x) > 0 \quad \forall x \in (a, b)$ فإن الدالة $f$ تكون متزايدة في $[a, b]$ .

2) $f'(x) < 0 \quad \forall x \in (a, b)$ فإن الدالة $f$ تكون متناقصة في $[a, b]$ .

3) $f'(x) = 0 \quad \forall x \in (a, b)$ فإن الدالة $f$ تكون ثابتة في $[a, b]$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
**مثال (1)**

ابحث اطراد الدالة $f(x) = x^2 + 5$ .

**الحل**

$\because f(x) = x^2 + 5$

متصلة، وقابلة للاشتقاق في مجالها $\mathbb{R}$ ،

$$f'(x) = 2x$$

$\because f'(x) > 0 \Rightarrow 2x > 0 \Rightarrow x > 0$

$\therefore$ الدالة متزايدة في الفترة $[0, \infty)$ .

وبالمثل $f'(x) < 0 \rightarrow 2x < 0 \Rightarrow x < 0$

$\therefore$ الدالة متناقصة في الفترة $(-\infty, 0]$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
**تدريب (1)**

ابحث اطراد كل دالة مما يأتي في مجالها:

$$f(x) = x^2 - 2x + 5 \quad \text{(a}$$

$$f(x) = 3 + 6x - 2x^2 \quad \text{(b}$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
**النقاط الحرجة**

**تعريف:**
لتكن الدالة $f$ متصلة في $[a, b]$ ، وكانت $x_0 \in (a, b)$ ، وكان $f'(x_0) = 0$ أو $f'(x_0)$ غير معرفة، فإن النقطة $(x_0, f(x_0))$ تسمى نقطة حرجة للدالة $f$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
72  الفصل 2 تطبيقات المشتقة
</div>
<!-- PAGE_END_72 -->


<!-- PAGE_START_73 -->
### صفحة 73

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 2</strong><br>
أوجد النقاط الحرجة للدالة $f(x) = 2x^3 - 3x^2 + 5$ في مجالها.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #ccc; padding: 8px; margin: 10px 0; background-color: #ffffdd; width: 220px; float: left;">
<strong>فكّر</strong><br>
هل توجد نقطة حرجة للدالة $f(x) = |x|$ عند النقطة $(0, 0)$، لماذا؟
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>

$$\because f(x) = 2x^3 - 3x^2 + 5$$

كثيرة حدود، ومجالها $\mathbb{R}$

$$\therefore f'(x) = 6x^2 - 6x$$

النقاط الحرجة تتواجد عند النقاط التي تحقق $f'(x) = 0$.

$$\therefore 6x^2 - 6x = 0 \Rightarrow 6x (x - 1) = 0$$

$$\Rightarrow x = 0 \text{ أو } x = 1$$

$$\therefore \text{النقاط الحرجة للدالة } f(x) \text{ هي } (0, 5) \text{ ، } (1, 4)$$
</div>

<div style="clear: both;"></div>

<hr style="border: 0.5px dashed #ccc; margin: 15px 0;">

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 2</strong><br>
أوجد النقاط الحرجة للدالة $f(x) = (x^2 - 2x - 8)^2$.
</div>

<br>

<div dir="rtl" style="text-align: center; font-size: 18px; font-weight: bold; background-color: #00aaff; color: white; padding: 5px; margin: 10px 0;">
النقاط العظمى والصغرى المحلية
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 2px solid #800080; padding: 10px; border-radius: 8px; background-color: #f9f0ff;">
<strong>تعريف</strong><br>
لتكن الدالة $f$ متصلة في $[a, b]$ ، $(x \in (a, b))$
<br><br>
1) يقال إن للدالة $f$ قيمة صغرى محلية $f(x_0)$ ، إذا أمكن إيجاد عدد $k > 0$ ، بحيث يكون:

$$f(x_0) \le f(x) \quad \forall x \in (x_0 - k, x_0 + k)$$

وفي هذه الحالة تسمى النقطة $(x_0, f(x_0))$ نقطة صغرى محلية للدالة $f$.
<br><br>
2) يقال إن للدالة $f$ قيمة عظمى محلية $f(x_0)$ ، إذا أمكن إيجاد عدد $k > 0$ ، بحيث يكون:

$$f(x_0) \ge f(x) \quad \forall x \in (x_0 - k, x_0 + k)$$

وفي هذه الحالة تسمى النقطة $(x_0, f(x_0))$ نقطة عظمى محلية للدالة $f$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
والشكل المجاور يوضح هذا التعريف.<br>
في الشكل المجاور توجد قيمة صغرى محلية للدالة المبينة عند كل من $x_1 , x_3 , x_5 , x_7$ ،<br>
وتوجد قيمة عظمى محلية عند كل من $x_2 , x_4 , x_6$ ، وذلك بالنسبة للفترة $[a, b]$.
</div>

<br><br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية | <strong>73</strong>
</div>
<!-- PAGE_END_73 -->


<!-- PAGE_START_74 -->
### صفحة 74

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويلاحظ أن $x_0 \in (x_7, b)$ أو $x_0 \in (x_4, x_5)$ ، يوجد عندها قيم عظمى محلية، وصغرى محلية في آن واحد.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>بدون برهان</strong>

<strong>نظرية:</strong> لتكن الدالة $f$ متصلة في $[a, b]$ ، ولها قيمة صغرى، أو عظمى محلية عند $x_0 \in (a, b)$ ، وكانت $f'(x_0)$ لها وجود، فإن $f'(x_0) = 0$ .
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>ملاحظات:</strong>
<ul>
<li>
في الشكل المجاور يلاحظ أنه إذا كانت $(x_0, f(x_0))$ نقطة عظمى محلية، فإن قبل $x_0$ مباشرة تكون الدالة $f$ مطردة التزايد أي أن
$$f'(x) > 0$$
وبعد $x_0$ مباشرة تكون الدالة $f$ مطردة التناقص أي أن
$$f'(x) < 0$$
</li>
<li>
إذا كانت $(x_0, f(x_0))$ نقطة صغرى محلية، فإن قبل $x_0$ مباشرة تكون الدالة $f$ مطردة التناقص أي أن
$$f'(x) < 0$$
وبعد $x_0$ مباشرة تكون الدالة $f$ مطردة التزايد أي أن
$$f'(x) > 0$$
</li>
</ul>
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
وتسمى هذه الطريقة "الاختبار باستعمال المشتقة الأولى" فمثلاً، الشكل أعلاه يُمثّل دالة متزايدة في $[a, c]$ ، $[d, b]$ ، ومتناقصة في الفترة $[c, d]$ ، وتُمثّل $(c, f(c))$ نقطة عظمى محلية، و $(d, f(d))$ نقطة صغرى محلية.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<ul>
<li>
قد يكون $f'(x_0) = 0$ ومع ذلك فإن $f(x_0)$ لا تكون قيمة عظمى محلية أو صغرى محلية، وهذا يعني أن النقطة الحرجة لا تكون بالضرورة نقطة عظمى، أو صغرى محلية، ويمكن ملاحظة ذلك في الشكل المجاور.
</li>
</ul>
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الفصل 2</strong> تطبيقات المشتقة | <strong>74</strong>
</div>
<!-- PAGE_END_74 -->


<!-- PAGE_START_75 -->
### صفحة 75

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="float: left; background-color: #2b6cb0; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold; margin-left: 10px;">مثال 3</span>
أوجد النقاط الحرجة إن وجدت للدالة $f(x) = x^3 - 9x^2 + 24x$، وحدّد فترات التزايد والتناقص، والنقاط الصغرى والعظمى المحلية.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; color: #2b6cb0; font-weight: bold;">
الحل
</div>

$$\because f(x) = x^3 - 9x^2 + 24x$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
دالة كثيرة الحدود، فهي متصلة وقابلة للاشتقاق $\forall x \in \mathbb{R}$
</div>

$$\therefore f'(x) = 3x^2 - 18x + 24 ,$$

$$f'(x) = 0$$

$$\Rightarrow 3(x^2 - 6x + 8) = 0$$

$$\Rightarrow (x - 2)(x - 4) = 0$$

$$\Rightarrow x = 2 \text{ أو } x = 4$$

$$\therefore f(2) = 8 - 9(4) + 24(2) = 20 ,$$

$$f(4) = 64 - 9(16) + 24(4) = 16$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ كل من النقطتين $(2, 20)$ ، $(4, 16)$ تُمثّل نقطة حرجة.
<br>
ومن دراسة إشارة $f'(x)$ حول كلّ من $x = 2$ ، $x = 4$ كما في الجدول المجاور نجد أن $(2, 20)$ تُمثّل نقطة عظمى محلية والقيمة العظمى المحلية هي $20$، بينما النقطة $(4, 16)$ تُمثّل نقطة صغرى محلية، والقيمة الصغرى المحلية هي $16$.
<br>
إذا تأملنا الجدول المجاور نلاحظ أن الدالة متزايدة في الفترتين $(-\infty, 2]$ و $[4, \infty)$ ، ومتناقصة في الفترة $[2, 4]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

| قيم $x$ | $-\infty$ | | $2$ | | $4$ | | $\infty$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **إشارة $f'(x)$** | | $+$ | | $-$ | | $+$ | |
| **اطراد الدالة $f(x)$** | | متزايدة $\nearrow$ | عظمى محلية | متناقصة $\searrow$ | صغرى محلية | متزايدة $\nearrow$ | |

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px; color: #555;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية &nbsp;&nbsp;&nbsp;&nbsp; <strong>75</strong>
</div>
<!-- PAGE_END_75 -->


<!-- PAGE_START_76 -->
### صفحة 76

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 4:</b> أوجد النقاط الحرجة للدالة $f(x) = \frac{3}{2}x^4 + 2x^3 - 3x^2 - 6x + \frac{9}{2}$ مبينًا نوعها، ثم ادرس اطراد الدالة.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل:</b><br>
$\because$ الدالة كثيرة حدود، فهي متصلة وقابلة للاشتقاق $\forall x \in \mathbb{R}$
</div>

$$\therefore f'(x) = 6x^3 + 6x^2 - 6x - 6$$

$$f'(x) = 0$$

$$\Rightarrow 6(x^3 + x^2 - x - 1) = 0$$

$$\Rightarrow (x^3 + x^2) - (x + 1) = 0$$

$$\Rightarrow x^2(x + 1) - (x + 1) = 0$$

$$\Rightarrow (x + 1)(x^2 - 1) = 0$$

$$\Rightarrow x = -1 \text{ أو } x = 1$$

$$\therefore f(-1) = \frac{3}{2} - 2 - 3 + 6 + \frac{9}{2} = 7$$

$$f(1) = \frac{3}{2} + 2 - 3 - 6 + \frac{9}{2} = -1$$

<br>

<!-- جدول دراسة إشارة f'(x) واطراد الدالة -->
<div dir="rtl" style="text-align: right; font-size: 16px;">
<table border="1" style="border-collapse: collapse; text-align: center; width: 60%; margin: 10px auto;">
  <tr>
    <th style="padding: 5px;">قيم $x$</th>
    <th colspan="2" style="padding: 5px;">$-1$</th>
    <th colspan="2" style="padding: 5px;">$1$</th>
    <th style="padding: 5px;"></th>
  </tr>
  <tr>
    <td style="padding: 5px;">إشارة كل من:<br>• $(x + 1)$<br>• $(x^2 - 1)$</td>
    <td style="padding: 5px;">$-$<br>$+$</td>
    <td style="padding: 5px;"></td>
    <td style="padding: 5px;">$+$<br>$-$</td>
    <td style="padding: 5px;"></td>
    <td style="padding: 5px;">$+$<br>$+$</td>
  </tr>
  <tr>
    <td style="padding: 5px;">إشارة $f'(x)$</td>
    <td style="padding: 5px;">$-$</td>
    <td style="padding: 5px;"></td>
    <td style="padding: 5px;">$-$</td>
    <td style="padding: 5px;"></td>
    <td style="padding: 5px;">$+$</td>
  </tr>
  <tr>
    <td style="padding: 5px;">اطراد الدالة $f(x)$</td>
    <td style="padding: 5px;">متناقصة $\searrow$</td>
    <td style="padding: 5px;"></td>
    <td style="padding: 5px;">متناقصة $\searrow$</td>
    <td style="padding: 5px; color: red;">صغرى محلية</td>
    <td style="padding: 5px; color: blue;">متزايدة $\nearrow$</td>
  </tr>
</table>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
من الجدول المجاور عند دراسة إشارة $f'(x)$ يتضح أن:<br>
النقطة الحرجة $(1, -1)$ نقطة صغرى محلية، أما النقطة الحرجة $(-1, 7)$ ، فإن المشتقة لا تغيّر إشارتها حولها، وبالتالي فهي ليست نقطة عظمى محلية، أو نقطة صغرى محلية.<br>
والدالة $f$ متناقصة في الفترة $(-\infty, 1]$ ، ومتزايدة في الفترة $[1, \infty)$ .
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 5:</b> أوجد قيم $b, c, d$ ، بحيث يحقق منحنى الدالة $f(x) = x^3 + bx^2 + cx + d$ الشرطين الآتيين:<br>
<b>a)</b> يمر بنقطة الأصل.<br>
<b>b)</b> له نقطة حرجة عند النقطة $(4, 16)$ .
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل:</b><br>
$\because$ المنحنى يمر بنقطة الأصل، فهي تحقق معادلته.
</div>

<br>

<div dir="rtl" style="text-align: left; font-size: 14px; font-weight: bold;">
الفصل 2 تطبيقات المشتقة &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 76
</div>
<!-- PAGE_END_76 -->


<!-- PAGE_START_77 -->
### صفحة 77

<div dir="rtl" style="text-align: right; font-size: 16px;">

$$\therefore 0 = 0 + 0 + 0d \Rightarrow d = 0 \qquad ......(1$$

$$\text{والمنحنى يمر بالنقطة } (4, 16)$$

$$\therefore 16 = 64 + b (16) + c (4) + 0$$

$$\Rightarrow -48 = 16b + 4c \Rightarrow -12 = 4b + c \qquad ......(2$$

$\because$ للمنحنى نقطة حرجة عند $x = 4$.

$$\therefore f'(4) = 0 ,$$

$$\because f'(x) = 3x^2 + 2bx + c$$

$$\therefore 0 = 3(4)^2 + 2b(4) + c$$

$$\Rightarrow -48 = 8b + c \qquad ......(3$$

بطرح المعادلة $(2)$ من المعادلة $(3)$ ينتج أن:

$$-36 = 4b \Rightarrow b = -9$$

بالتعويض عن قيمة $b$ في المعادلة $(2)$ ينتج أن:

$$-12 = -36 + c \Rightarrow c = 24$$

$$\therefore b = -9 \quad , \quad c = 24 \quad , \quad d = 0$$

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">

### **تدريب 3**

أوجد النقاط الحرجة للدالة $f(x) = x^3 + x^2 - 5x + 3$ ، وحدد فترات التزايد والتناقص، والنقاط الصغرى والعظمى المحلية.

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">

### **تقعر المنحنيات**

**تعريف:**
إذا كانت $f$ دالة معرفة على الفترة $[a, b]$، فإنه:

1) يقال أن منحنى الدالة $f$ **مقعر إلى أعلى في $(a, b)$**، إذا كان واقعاً بتمامه فوق مماسّاته في هذه الفترة.

2) يقال أن منحنى الدالة $f$ **مقعر إلى أسفل في $(a, b)$**، إذا كان واقعاً بتمامه أسفل مماسّاته في هذه الفترة.

<br>

ففي **الشكل a** منحنى الدالة $f$ مقعر إلى أعلى وفي **الشكل b** منحنى الدالة $f$ مقعر إلى أسفل.

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية | 77
</div>
<!-- PAGE_END_77 -->


<!-- PAGE_START_78 -->
### صفحة 78

<div dir="rtl" style="text-align: right; font-size: 16px;">
### نقاط الانقلاب
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
**تعريف:**
تسمى النقطة $(x, f(x))$ **نقطة انقلاب (انعطاف)**، إذا كان المنحنى يغير اتجاه تقعره عندها سواء من مقعر إلى أعلى إلى مقعر إلى أسفل، أو من مقعر إلى أسفل إلى مقعر إلى أعلى.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
لاحظ الشكلين أدناه:
</div>

<!-- الشكل البياني يتضمن منحنيين يوضحان نقاط الانقلاب -->

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
**نظرية (بدون برهان):**

إذا كانت الدالة $f$ متصلة في الفترة $[a, b]$، وقابلة للاشتقاق حتى المشتقة الثانية في $(a, b)$، فإن:

1) يكون منحنى الدالة $f$ مقعراً إلى أعلى في $(a, b)$، إذا كانت:
$$f''(x) > 0 \quad \forall x \in (a, b)$$

2) يكون منحنى الدالة $f$ مقعراً إلى أسفل في $(a, b)$، إذا كانت:
$$f''(x) < 0 \quad \forall x \in (a, b)$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
**نظرية (بدون برهان):**

إذا كان لمنحنى الدالة $f$ نقطة انقلاب عند النقطة $(x_0, f(x_0))$، فإن $f''(x_0) = 0$.
</div>
<!-- PAGE_END_78 -->


<!-- PAGE_START_79 -->
### صفحة 79

<div dir="rtl" style="text-align: right; font-size: 16px;">

**[مثال 6]**

أوجد نقاط الانقلاب إن وجدت لمنحنى الدالة $f(x) = x^3$ ، وحَدّد الفترة التي يكون فيها منحنى الدالة مقعراً إلى أعلى، والفترة التي يكون فيها مقعراً إلى أسفل.

**الحل:**

$$\because f(x) = x^3$$

$\therefore$ الدالة $f$ متصلة، وقابلة للاشتقاق في $\mathbb{R}$.

$$f'(x) = 3x^2 \quad , \quad f''(x) = 6x$$

$$f''(x) = 0$$

$$\Rightarrow 6x = 0$$

$$\Rightarrow x = 0$$

$$\Rightarrow f(0) = 0$$

ويدراسة إشارة $f''(x)$ حول $x = 0$ كما في الجدول أعلاه، نجد أن:

$$f''(x) < 0 \quad \forall x \in (-\infty, 0)$$

أي أن منحنى الدالة $f$ مقعر إلى أسفل في $(-\infty, 0)$.

وبالمثل $f''(x) > 0 \quad \forall x \in (0, \infty)$ ؛ أي أن منحنى الدالة $f$ مقعر إلى أعلى في $(0, \infty)$.

$\therefore$ النقطة $(0, 0)$ نقطة انقلاب.

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

| قيم $x$ | $-\infty$ | $0$ | $\infty$ |
| :---: | :---: | :---: | :---: |
| إشارة $f''(x)$ | $-$ | | $+$ |
| اتجاه تقعر منحنى الدالة $f(x)$ | مقعر إلى أسفل | | مقعر إلى أعلى |

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

والنظرية الآتية توضح كيفية استعمال المشتقة الثانية؛ لاختبار نوع النقاط الحرجة من حيث كونها عظمى محلية أو صغرى محلية، وتسمى هذه طريقة **"الاختبار باستعمال المشتقة الثانية"**.

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 2px solid #00a651; padding: 15px; background-color: #f9f9f9; border-radius: 8px;">

**[نظرية] الاختبار باستعمال المشتقة الثانية**

إذا كانت $(x_0, f(x_0))$ نقطة حرجة للدالة $f$ ، حيث $f'(x_0) = 0$ ، فإن:

**a)** إذا كانت $f''(x_0) > 0$ ، فإن للدالة $f$ قيمة صغرى محلية عند $x_0$ .

**b)** إذا كانت $f''(x_0) < 0$ ، فإن للدالة $f$ قيمة عظمى محلية عند $x_0$ .

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

والشكل أعلاه يوضح هذه النظرية.

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #ffcc00; padding: 10px; background-color: #fffde7; border-radius: 5px;">

**ملاحظة:**
النظرية السابقة لم تتعرض للحالات التي يكون فيها $f''(x_0) = 0$ ، أو غير معرفة، وفي مثل هذه الحالات ندرس إشارة المشتقة الأولى على جانبي $x_0$ لتحديد نوعها.

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 79
</div>
<!-- PAGE_END_79 -->


<!-- PAGE_START_80 -->
### صفحة 80

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 7:</strong><br>
أوجد نقاط الانقلاب إن وجدت لمنحنى الدالة $f(x) = x^4 - 6x^2 - 7$ ، وحدد الفترة التي يكون فيها منحنى الدالة مقعرًا إلى أعلى، والفترة التي يكون فيها مقعرًا إلى أسفل، ثم بيّن نوع النقاط الحرجة باستعمال المشتقة الثانية.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
$\because$ الدالة $f$ كثيرة حدود ، فهي متصلة وقابلة للاشتقاق في $\mathbb{R}$.
</div>

$$\because f'(x) = 4x^3 - 12x \quad ,$$

$$f''(x) = 12x^2 - 12 \quad ,$$

$$f''(x) = 0$$

$$\Rightarrow 12x^2 - 12 = 0$$

$$\Rightarrow x^2 - 1 = 0$$

$$\Rightarrow (x - 1)(x + 1) = 0$$

$$\Rightarrow x = 1 \text{ أو } x = -1$$

$$\Rightarrow f(1) = -12 \quad ,$$

$$f(-1) = -12$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ النقطتان $(1, -12)$ ، $(-1, -12)$ هما نقطتا انقلاب. وبدراسة إشارة $f''(x)$ حول كل من $x = -1, x = 1$ كما في الجدول المجاور نجد أن:<br>
منحنى الدالة $f$ مقعر إلى أسفل في $(-1, 1)$ ،<br>
ومنحنى الدالة $f$ مقعر إلى أعلى في $(-\infty, -1) \cup (1, \infty)$ أو $\mathbb{R} \setminus [-1, 1]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<table border="1" style="border-collapse: collapse; text-align: center; width: 100%; margin-top: 10px;">
  <tr>
    <td style="padding: 8px;"><strong>قيم $x$</strong></td>
    <td style="padding: 8px;">$-\infty$</td>
    <td style="padding: 8px;" colspan="2">$-1$</td>
    <td style="padding: 8px;" colspan="2">$1$</td>
    <td style="padding: 8px;">$\infty$</td>
  </tr>
  <tr>
    <td style="padding: 8px;"><strong>إشارة $f''(x)$</strong></td>
    <td style="padding: 8px;" colspan="2">$+$</td>
    <td style="padding: 8px;" colspan="2">$-$</td>
    <td style="padding: 8px;" colspan="2">$+$</td>
  </tr>
  <tr>
    <td style="padding: 8px;"><strong>اتجاه تقعر منحنى الدالة $f(x)$</strong></td>
    <td style="padding: 8px;" colspan="2">مقعر إلى أعلى</td>
    <td style="padding: 8px;" colspan="2">مقعر إلى أسفل</td>
    <td style="padding: 8px;" colspan="2">مقعر إلى أعلى</td>
  </tr>
</table>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>80</strong> &nbsp;&nbsp;&nbsp;&nbsp; <strong>الفصل 2 تطبيقات المشتقة</strong>
</div>
<!-- PAGE_END_80 -->


<!-- PAGE_START_81 -->
### صفحة 81

<div dir="rtl" style="text-align: right; font-size: 16px;">
وباستعمال النظرية السابقة نجد أن:
</div>

$$\because f'(x) = 4x^3 - 12x$$
$$f'(x) = 0$$
$$\therefore 4x^3 - 12x = 0$$
$$\Rightarrow 4x(x^2 - 3) = 0$$
$$\Rightarrow x = 0 \text{ أو } x = \pm\sqrt{3}$$
$$f''(x) = 12x^2 - 12$$
$$\Rightarrow f''(0) = -12 < 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ للدالة $f$ نقطة عظمى محلية عند $(0, -7)$.
<br>
وبالمثل $f''(-\sqrt{3}) = f''(\sqrt{3}) = 24 > 0$
<br>
$\therefore$ للدالة $f$ نقطة صغرى محلية عند كل من $(-\sqrt{3}, -16)$ ، $(\sqrt{3}, -16)$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 4</strong>
<br>
أوجد نقاط الانقلاب إن وجدت لمنحنى الدالة $f(x) = 1 - 3x^2 + 2x^3$ ، وحدّد الفترة التي يكون فيها منحنى الدالة مقعّراً إلى أعلى، والفترة التي يكون فيها مقعّراً إلى أسفل، ثم بيّن نوع النقاط الحرجة باستعمال المشتقة الثانية.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية | 81
</div>
<!-- PAGE_END_81 -->


<!-- PAGE_START_82 -->
### صفحة 82

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 8:</strong><br>
عيّن قيمة كلّ من $a, b$ لكي يكون للدالة $f(x) = x^3 + ax^2 + bx$ نقطة حرجة عند $x = 2$، ونقطة انقلاب عند $x = \frac{1}{2}$، ثم عين القيم العظمى والصغرى المحلية لهذه الدالة.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ الدالة $f$ كثيرة حدود ، فهي متصلة وقابلة للاشتقاق في $\mathbb{R}$
</div>

$$\therefore f'(x) = 3x^2 + 2ax + b$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ عند النقطة الحرجة تكون $f'(x) = 0$
</div>

$$\therefore f'(2) = 0$$
$$\Rightarrow 12 + 4a + b = 0 \dots\dots\dots (1)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ عند نقطة الانقلاب تكون $f''(x) = 0$
</div>

$$\therefore f''(x) = 6x + 2a = 0$$
$$\Rightarrow f''\left(\frac{1}{2}\right) = 3 + 2a = 0$$
$$\Rightarrow a = \frac{-3}{2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
بالتعويض في المعادلة (1) ينتج أن:
</div>

$$12 + 4\left(\frac{-3}{2}\right) + b = 0$$
$$\Rightarrow 12 - 6 + b = 0$$
$$\Rightarrow b = -6$$

$$\therefore f(x) = x^3 - \frac{3}{2}x^2 - 6x$$
$$f'(x) = 3x^2 - 3x - 6$$
$$= 3(x^2 - x - 2)$$
$$= 3(x - 2)(x + 1)$$
$$f'(x) = 0$$
$$\Rightarrow 3(x - 2)(x + 1) = 0$$
$$\Rightarrow x = 2 \quad \text{أو} \quad x = -1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ للدالة نقطتان حرجتان هما $\left(-1, \frac{7}{2}\right) , (2, -10)$
</div>

$$f''(x) = 6x - 3$$
$$\because f''(2) = 9 > 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ للدالة $f$ قيمة صغرى محلية تساوي $(-10)$ عندما $x = 2$.<br>
وبالمثل $f''(-1) = -9 < 0$<br>
$\therefore$ للدالة $f$ قيمة عظمى محلية تساوي $\left(\frac{7}{2}\right)$ عندما $x = -1$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>الفصل 2 تطبيقات المشتقة</strong> <span style="float: left;"><strong>82</strong></span>
</div>
<!-- PAGE_END_82 -->


<!-- PAGE_START_83 -->
### صفحة 83

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمرينات (4-2)</h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد النقاط الحرجة إن وجدت مبيناً نوعها، ثم ادرس اطراد كل دالة مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
1) $f(x) = 1 - (x - 2)^2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2) $f(x) = 2x^3 - 3x^2 - 12x - 5$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3) $f(x) = x^3 - 8$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
4) $f(x) = (x - 2)^3 + 3$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
5) $f(x) = \frac{1}{2}x^4 + x^3 - 4x^2 - 12x$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
6) إذا كان للدالة $f(x) = ax^3 + bx^2 + 9x + 1$ قيمة عظمى محلية عند $x = 1$، وقيمة صغرى محلية عند $x = 3$، فما قيمة كل من $a , b$؟
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
7) أوجد معادلة المنحنى كثير الحدود من الدرجة الثانية والذي يمر بالنقطتين $(0,0)$ ، $(2,12)$، وله نقطة حرجة عند $x = 2$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
8) إذا كانت $f(x) = ax^3 + bx^2 - 12x$، وكان لمنحنى الدالة $f(x)$ نقطة حرجة عند $(1,0)$ الواقعة على منحنى $f(x)$، فعيّن الثابتين $a , b$.
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد نقاط الانقلاب إن وجدت لمنحنى كلٍّ من الدوال الآتية، وحدّد الفترة التي يكون فيها منحنى الدالة مقعراً إلى أعلى، والفترة التي يكون فيها مقعراً إلى أسفل، ثم بيّن نوع النقاط الحرجة باستعمال المشتقة الثانية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
9) $f(x) = (x - 2)^2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
10) $f(x) = x^3 - 3x^2 - 9x + 5$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
11) $f(x) = (x - 3)^3$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
12) $f(x) = 4x^3 - x^4$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
13) $f(x) = \frac{1}{4}x^4 + \frac{1}{3}x^3 - 8x^2 - 16x + 1$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
14) عيّن الثابتين $a , b$ لكي يكون للدالة:
$$f(x) = ax^3 + bx^2 + 6x + 2$$
نقطة حرجة عند $x = 1$، وكذلك نقطة انقلاب عند $x = 1$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
15) عيّن الثوابت $a , b , c$ لكي يكون للدالة $f(x) = ax^3 + bx^2 + cx$ نقطة حرجة عند $x = -1$، ونقطة انقلاب عند $x = \frac{1}{2}$، ويمر منحنى الدالة بالنقطة $(1,13)$.
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 4-2 تطبيقات المشتقة الأولى والثانية | 83
</div>
<!-- PAGE_END_83 -->


<!-- PAGE_START_84 -->
### صفحة 84

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>2-5 التمثيل البياني لمنحنيات دوال كثيرات الحدود</h2>
<strong>Graphing Polynomials</strong>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
يعتمد التمثيل البياني لمنحنى دالة ما على تحديد عدد مناسب من النقاط التي تحقق هذه الدالة، وعلى تحديد بعض معالم الدالة، من حيث التزايد والتناقص، ونقاط الانقلاب، ونقاط القيم العظمى والصغرى المحلية إن وجدت. وسوف يقتصر اهتمامنا فيما يأتي على تمثيل منحنيات دوال كثيرات الحدود بيانياً، والتي نعلم أنها متصلة وقابلة للاشتقاق على مجموعة الأعداد الحقيقية ($\mathbb{R}$)، أو على منحنيات دوال تؤول إلى ذلك.
<br><br>
وعند محاولة تمثيل منحنى الدالة $f$ بيانياً، فإننا:
<br>
<strong>a)</strong> نعين (إن أمكن) نقاط التقاطع مع المحورين، حيث $f(x) = 0$ مع المحور $x$، وحيث $(x = 0)$ مع المحور $y$.
<br>
<strong>b)</strong> نعين النقاط الحرجة والنقاط العظمى والصغرى المحلية بالاستفادة من المشتقة الأولى والثانية، كما ويساعدنا معرفة المشتقة الأولى أن نعرف متى تكون الدالة متزايدة أو متناقصة.
<br>
<strong>c)</strong> تحديد اتجاه تقعر الدالة بالاستعانة بالمشتقة الثانية، والمثال الآتي يوضح ذلك.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1:</strong>
<br>
إذا كانت الدالة $f(x) = x(x - 3)^2$ ، فحدد فترات التزايد والتناقص، والنقاط العظمى والصغرى المحلية إن وجدت، ونقاط الانقلاب إن وجدت، والفترة التي يكون فيها منحنى الدالة مقعراً إلى أعلى، والفترة التي يكون فيها مقعراً إلى أسفل، ثم مثل بيانياً منحنى الدالة بصورة تقريبية.
<br><br>
<strong>الحل</strong>
</div>

$$\because f(x) = x(x - 3)^2 = x^3 - 6x^2 + 9x$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدالة $f$ كثيرة حدود متصلة وقابلة للاشتقاق
</div>

$$\therefore f'(x) = 3x^2 - 12x + 9$$

$$f'(x) = 0$$

$$\Rightarrow 3(x^2 - 4x + 3) = 0$$

$$\Rightarrow (x - 3)(x - 1) = 0$$

$$\Rightarrow x = 1 \quad \text{أو} \quad x = 3$$

$$\Rightarrow f(3) = 0 , \quad f(1) = 4$$
<!-- PAGE_END_84 -->


<!-- PAGE_START_85 -->
### صفحة 85

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ النقطتان $(1, 4) ، (3, 0)$ نقطتان حرجتان.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن دراسة إشارة $f'(x)$ حول كل من: $x = 1 , x = 3$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
كما في الجدول المجاور نجد أن:
</div>

| قيم $x$ | $-\infty$ | | $1$ | | $2$ | | $3$ | | $\infty$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **إشارة $f'(x)$** | | $+$ | | $-$ | | $-$ | | $+$ | |
| **اطّراد الدالة $f(x)$** | | متزايدة | عظمى محلية | متناقصة | | متناقصة | صغرى محلية | متزايدة | |
| **إشارة $f''(x)$** | | $-$ | | $-$ | | $+$ | | $+$ | |
| **اتجاه تقعر منحنى الدالة $f(x)$** | | مقعر إلى أسفل | | مقعر إلى أسفل | | مقعر إلى أعلى | | مقعر إلى أعلى | |

<div dir="rtl" style="text-align: right; font-size: 16px;">
منحنى الدالة $f$ متناقص في الفترة $[1, 3]$ ، ومتزايد في الفترة $\mathbb{R} \setminus (1, 3)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
للدالة $f$ نقطة صغرى محلية عند $(3, 0)$، ونقطة عظمى محلية عند $(1, 4)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
لتحديد نقاط الانقلاب نوجد المشتقة الثانية.
</div>

$$f''(x) = 6x - 12$$

$$\because f''(x) = 0$$

$$\therefore 6x - 12 = 0$$

$$\Rightarrow x = 2$$

$$\Rightarrow f(2) = 2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ النقطة $(2, 2)$ نقطة انقلاب.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبدراسة إشارة $f''(x)$ حول $x = 2$ كما في الجدول أعلاه نجد أن:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
منحنى الدالة $f$ مقعر إلى أعلى في الفترة $(2, \infty)$، ومقعر إلى أسفل في الفترة $(-\infty, 2)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
ولتمثيل منحنى الدالة بيانياً، نحصر النقاط التي تم الحصول عليها، وهي النقطتان الحرجتان ونقطة الانقلاب، ونلاحظ أن هذه النقاط غير كافية لتحديد شكل منحنى الدالة $f$؛ لذا نلجأ لبعض النقاط المساعدة، ويُفضل اختيار نقاط التقاطع مع المحورين، وعليه فإن:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
• نقاط تقاطع منحنى الدالة $f$ مع المحور $x$ هي $(0, 0) ، (3, 0)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
• نقاط تقاطع منحنى الدالة $f$ مع المحور $y$ هي $(0, 0)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
النقطة $(3, 0)$ نقطة حرجة، ونقطة تقاطع منحنى الدالة مع المحور $x$؛ لذا يمكن اختيار نقاط أخرى تساعدنا لتمثيل المنحنى بيانياً كما هو في الجدول أدناه:
</div>

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | $0$ | $4$ | $2$ | $0$ | $4$ |

---

<div dir="rtl" style="text-align: center; font-size: 14px;">
الدرس 5-2 التمثيل البياني لمنحنيات دوال كثيرات الحدود | 85
</div>
<!-- PAGE_END_85 -->


<!-- PAGE_START_86 -->
### صفحة 86

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 2</b>
<br>
إذا كانت الدالة $f(x) = (x - 1)^3$، فحدّد فترات التزايد والتناقص، والنقاط العظمى والصغرى المحلية إن وجدت، ونقاط الانقلاب إن وجدت، والفترة التي يكون فيها منحنى الدالة مقعرًا إلى أعلى، والفترة التي يكون فيها مقعرًا إلى أسفل، ثم مثّل منحنى الدالة بيانيًا بصورة تقريبية.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
</div>

| قيم $x$ | $-\infty$ | $1$ | $\infty$ |
| :---: | :---: | :---: | :---: |
| **إشارة $f'(x)$** | $+$ | | $+$ |
| **اطراد الدالة $f(x)$** | متزايدة ↗ | | متزايدة ↗ |
| **إشارة $f''(x)$** | $-$ | | $+$ |
| **اتجاه تقعر منحنى الدالة $f(x)$** | مقعر إلى أسفل | | مقعر إلى أعلى |

$$\because f(x) = (x - 1)^3$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدالة $f$ كثيرة حدود متصلة وقابلة للاشتقاق،
</div>

$$\therefore f'(x) = 3(x - 1)^2$$
$$f'(x) = 0$$
$$3(x - 1)^2 = 0$$
$$x - 1 = 0$$
$$x = 1$$
$$f(1) = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ النقطة $(1, 0)$ نقطة حرجة.
<br>
ومن دراسة إشارة $f'(x)$ حول $x = 1$ كما في الجدول أعلاه نجد أن:
<br>
الدالة $f$ متزايدة في $\mathbb{R}$.
<br>
لا توجد للدالة قيم عظمى ولا صغرى محلية.
<br>
ولتحديد نقاط الانقلاب نوجد المشتقة الثانية للدالة:
</div>

$$f''(x) = 6(x - 1)$$
$$f''(x) = 0$$
$$6(x - 1) = 0$$
$$x = 1$$
$$f(1) = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ النقطة $(1, 0)$ نقطة انقلاب.
<br>
وبدراسة إشارة $f''(x)$ حول $x = 1$ كما في الجدول أعلاه نجد أن:
<br>
منحنى الدالة $f$ مقعر إلى أسفل في الفترة $(-\infty, 1)$، ومقعر إلى أعلى في الفترة $(1, \infty)$.
<br>
ولتمثيل منحنى الدالة $f$ بيانيًا، يمكن إيجاد نقاط مساعدة كما في الجدول أدناه.
</div>

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$f(x)$** | $-8$ | $-1$ | $0$ | $1$ | $8$ |

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 2 تطبيقات المشتقة <b>86</b>
</div>
<!-- PAGE_END_86 -->


<!-- PAGE_START_87 -->
### صفحة 87

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3</strong><br>
إذا كانت الدالة $f(x) = 12x - x^3 + 1$، فحدّد فترات التزايد والتناقص، والنقاط العظمى والصغرى المحلية إن وجدت، ونقاط الانقلاب إن وجدت، والفترة التي يكون فيها منحنى الدالة مقعراً إلى أعلى، والفترة التي يكون فيها مقعراً إلى أسفل، ثم مثّل منحنى الدالة بيانياً بصورة تقريبية.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
$\because$ الدالة $f$ كثيرة حدود متصلة وقابلة للاشتقاق
</div>

$$\therefore f'(x) = 12 - 3x^2$$

$$f'(x) = 0$$

$$\Rightarrow 12 - 3x^2 = 0$$

$$\Rightarrow 3(4 - x^2) = 0$$

$$\Rightarrow (2 - x)(2 + x) = 0$$

$$\Rightarrow x = 2 \quad \text{أو} \quad x = -2$$

$$\Rightarrow f(2) = 17 \quad , \quad f(-2) = -15$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore (2, 17) \text{ ، } (-2, -15)$ نقطتان حرجتان، ومن دراسة إشارة $f'(x)$ حول كل من:
$$x = 2 \quad , \quad x = -2$$
كما في الجدول أعلاه نجد أن:<br>
الدالة $f$ متزايدة في الفترة $[-2, 2]$ ، ومتناقصة في الفترة $\mathbb{R} \setminus (-2, 2)$<br>
القيمة العظمى المحلية هي $(17)$ عندما $x = 2$، القيمة الصغرى المحلية هي $(-15)$ عندما $x = -2$.<br>
ولتحديد نقاط الانقلاب نوجد المشتقة الثانية للدالة:
</div>

$$\therefore f''(x) = -6x$$

$$f''(x) = 0$$

$$\Rightarrow -6x = 0$$

$$\Rightarrow x = 0$$

$$\Rightarrow f(0) = 1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ النقطة $(0, 1)$ نقطة انقلاب.<br>
وبدراسة إشارة $f''(x)$ حول $(x = 0)$ كما في الجدول أعلاه نجد أن:<br>
منحنى الدالة مقعر إلى أعلى في الفترة $(-\infty, 0)$،<br>
ومقعر إلى أسفل في الفترة $(0, \infty)$.<br>
ولتمثيل منحنى الدالة $f$ بيانياً يمكن إيجاد نقاط مساعدة كما في الجدول أدناه.
</div>

<br>

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | $-8$ | $-15$ | $-10$ | $1$ | $12$ | $17$ | $10$ |

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>جدول دراسة الإشارة والتقعر:</strong>
</div>

| قيم $x$ | $-\infty$ | | $-2$ | | $0$ | | $2$ | | $\infty$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| إشارة $f'(x)$ | | $-$ | | $+$ | | $+$ | | $-$ | |
| اطراد الدالة $f(x)$ | | متناقصة ($\searrow$) | صغرى محلية | متزايدة ($\nearrow$) | | متزايدة ($\nearrow$) | عظمى محلية | متناقصة ($\searrow$) | |
| إشارة $f''(x)$ | | $+$ | | $+$ | | $-$ | | $-$ | |
| اتجاه تقعر منحنى الدالة $f(x)$ | | مقعر إلى أعلى ($\cup$) | | مقعر إلى أعلى ($\cup$) | نقطة انقلاب | مقعر إلى أسفل ($\cap$) | | مقعر إلى أسفل ($\cap$) | |

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 5-2 التمثيل البياني لمنحنيات دوال كثيرات الحدود 87
</div>
<!-- PAGE_END_87 -->


<!-- PAGE_START_88 -->
### صفحة 88

<div dir="rtl" style="text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 20px;">
تمارين (5-2)
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
حدّد فترات التزايد والتناقص، والنقاط العظمى والصغرى المحلية إن وجدت، ونقاط الانقلاب إن وجدت، والفترة التي يكون فيها منحنى الدالة مقعرًا إلى أعلى، والفترة التي يكون فيها مقعرًا إلى أسفل لمنحنى كل من الدوال الآتية، ثم مثّل منحنى الدالة بيانيًا بصورة تقريبية:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

1. 
$$f(x) = x^3$$

2. 
$$f(x) = x^3 - 4x^2 + 4x$$

3. 
$$f(x) = 3x^2 - x^3$$

4. 
$$f(x) = (1 - x)^3$$

5. 
$$f(x) = x(x - 3)^2 + 1$$

6. 
$$f(x) = (x + 1)^2 (x - 2) + 5$$

7. 
$$f(x) = (x - 1)(x - 2)(x - 3)$$

</div>

<br><hr><br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>88</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>الفصل 2 تطبيقات المشتقة</b>
</div>
<!-- PAGE_END_88 -->


<!-- PAGE_START_89 -->
### صفحة 89

<div dir="rtl" style="text-align: right; font-size: 16px;">

# 2-6 تطبيقات على القيم العظمى والصغرى
<p dir="ltr" style="text-align: left;"><b>Applications of Maximum and Minimum Values</b></p>

في كثير من المسائل الرياضية والعلمية من المهم إيجاد أكبر قيم للدالة وأصغرها. مثال ذلك أكبر ربح وأقل خسارة، أقل مساحة وأكبر حجم .... إلخ.

إن الحساب التفاضلي يقدم لنا الطرق الناجحة؛ لإيجاد أكبر القيم وأقلها، وفيما يأتي بعض الأمثلة على ذلك:

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #0056b3; padding: 12px; border-radius: 5px; background-color: #f9f9f9;">

**مثال 1:**

عددان موجبان مجموعهما $20$ ، أوجد العددين إذا كان:

**a)** حاصل ضربهما أكبر ما يمكن.  
**b)** مجموع مربعيهما أصغر ما يمكن.

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

<h3 style="color: #b30000;">الحل:</h3>

**a)** افرض أن العددين هما:

$$x \quad , \quad 20 - x \quad , \quad x \in (0, 20)$$

ونرمز لحاصل ضرب العددين بالرمز $P(x)$

$$\therefore P(x) = x (20 - x)$$
$$= 20 x - x^2 \quad , \quad 0 < x < 20$$

$$\therefore P'(x) = 20 - 2x$$

حاصل ضرب العددين يكون أكبر ما يمكن عندما يكون:

$$P'(x) = 0$$
$$\Rightarrow 20 - 2x = 0$$
$$\Rightarrow x = 10,$$

$$P''(10) = -2 < 0 \quad \text{لماذا؟}$$

لحاصل ضرب العددين $P(x)$ قيمة عظمى عندما $x = 10$.

$\therefore$ العددان هما $10 \quad , \quad 10$

<br>

**b)** نرمز لمجموع مربعي العددين بالرمز $D(x)$

$$\therefore D(x) = x^2 + (20 - x)^2$$
$$D'(x) = 2x - 2(20 - x)$$
$$= 4x - 40$$

</div>

<br><hr>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>89</b> | الدرس 6-2 تطبيقات على القيم العظمى والصغرى
</div>
<!-- PAGE_END_89 -->


<!-- PAGE_START_90 -->
### صفحة 90

<div dir="rtl" style="text-align: right; font-size: 16px;">
مجموع مربعي العددين $D(x)$ يكون أصغر ما يمكن عندما تكون:
</div>

$$D'(x) = 0$$
$$\Rightarrow 4x - 40 = 0$$
$$\Rightarrow x = 10$$
$$D''(10) = 4 > 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
لمجموع مربعي العددين قيمة صغرى عندما $x = 10$
<br>
$\therefore$ العددان هما $10 , 10$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2):</strong>
<br>
يراد صنع صندوق مفتوح من أعلى باستعمال قطعة من الكرتون مستطيلة عرضها $8\text{ cm}$ وطولها $15\text{ cm}$، بقطع مربعات متساوية عند رؤوسها، ثم ثني الأجزاء البارزة إلى أعلى.
<br>
أوجد أكبر حجم صندوق يمكن صنعه بهذه الطريقة.
<br>
(علماً بأن حجم الصندوق = الطول $\times$ العرض $\times$ الارتفاع).
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
<br>
افرض أن طول ضلع المربع $x$ بالسنتيمترات كما في الشكل أدناه، فتكون قاعدة الصندوق بعد الثني مستطيلة الشكل، وأبعادها $(15 - 2x)\text{ cm}$ ، $(8 - 2x)\text{ cm}$، ويكون ارتفاع الصندوق $x$ بالسنتيمترات، إذا رمزنا لحجم الصندوق بالرمز $V$ بالسنتيمترات المكعبة يكون:
</div>

$$V(x) = (15 - 2x)(8 - 2x)(x) \quad , \quad 0 < x < 4$$
$$= 120x - 46x^2 + 4x^3$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
يكون حجم الصندوق $V(x)$ أكبر ما يمكن عندما $V'(x) = 0$
</div>

$$\Rightarrow 120 - 92x + 12x^2 = 0$$
$$\Rightarrow 30 - 23x + 3x^2 = 0$$
$$\Rightarrow (5 - 3x)(6 - x) = 0$$
$$\Rightarrow x = \frac{5}{3} \quad \text{أو} \quad x = 6 \quad (\text{مرفوض } 6 \notin (0, 4))$$

$$V''(x) = -92 + 24x$$
$$V''\left(\frac{5}{3}\right) = -92 + 24\left(\frac{5}{3}\right)$$
$$= -52 < 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ حجم الصندوق $V(x)$ يكون أكبر ما يمكن (قيمة عظمى) عندما $x = \frac{5}{3}$، ويكون حجم الصندوق عندئذٍ:
</div>

$$V\left(\frac{5}{3}\right) = \left(\frac{35}{3}\right)\left(\frac{14}{3}\right)\left(\frac{5}{3}\right)$$
$$= \frac{2450}{27} \text{ cm}^3$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>الفصل 2 تطبيقات المشتقة</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>90</strong>
</div>
<!-- PAGE_END_90 -->


<!-- PAGE_START_91 -->
### صفحة 91

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 3</b><br>
يراد صنع علبة معدنية على شكل أسطوانة دائريّة قائمة سعتها $1000\pi \text{ cm}^3$.<br>
أوجد أبعاد الأسطوانة؛ لتكون كمية المعدن المستعمل أقل ما يمكن:<br>
a) إذا كانت العلبة دون غطاء.<br>
b) إذا استعملت العلبة؛ لحفظ اللحوم.<br>
علماً بأن حجم الأسطوانة هو $V = \pi r^2 h$ ، والمساحة السطحية للأسطوانة تساوي المساحة الجانبية + مساحة القاعدتين؛ أي أن $A = 2\pi rh + 2\pi r^2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b><br>
a) إذا كانت العلبة دون غطاء
</div>

$$V = 1000\pi \quad \text{............. (1)}$$
$$A = 2\pi rh + \pi r^2 \quad \text{.......... (2)}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وهذه دالة في متغيّرين، ومن ثمّ يجب أن نجعل $A$ دالة متغيّر واحد وليكن ($r$) قبل الاشتقاق، ولهذه الغاية نحل المعادلة (1) ونعوّض في معادلة (2) فينتج أن:
</div>

$$h = \frac{1000\pi}{\pi r^2} = \frac{1000}{r^2} \quad \text{......... (3)}$$

$$\therefore A(r) = (2\pi r)\left(\frac{1000}{r^2}\right) + \pi r^2$$
$$= \frac{2000\pi}{r} + \pi r^2 , \quad r > 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
المساحة السطحية للأسطوانة ($A$) أكبر ما يمكن عندما:
</div>

$$A'(r) = 0$$
$$\Rightarrow A'(r) = \frac{-2000\pi}{r^2} + 2\pi r = 0$$
$$\Rightarrow \frac{2000\pi}{r^2} = 2\pi r$$
$$\Rightarrow 2\pi r^3 = 2000\pi$$
$$\Rightarrow r = 10\text{ cm}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالتعويض عن قيمة ($r$) في المعادلة (3) ينتج أن:
</div>

$$h = \frac{1000}{100} = 10\text{ cm}$$
$$A''(r) = \frac{4000\pi}{r^3} + 2\pi$$
$$A''(10) = \frac{4000\pi}{1000} + 2\pi$$
$$= 4\pi + 2\pi$$
$$= 6\pi > 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>91</b> | الدرس 6-2 تطبيقات على القيم العظمى والصغرى
</div>
<!-- PAGE_END_91 -->


<!-- PAGE_START_92 -->
### صفحة 92

<div dir="rtl" style="text-align: right; font-size: 16px;">
تكون المساحة السطحية للعلبة أقل ما يمكن عندما:
</div>

$$r = h = 10 \text{ cm}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن ثم فإن كمية المعدن المستعملة تكون أقل ما يمكن.
</div>

$$A = (2\pi)(10)(10) + (100\pi)$$
$$= 200\pi + 100\pi$$
$$= 300\pi \text{ cm}^2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>b)</b> إذا استعملت العلبة لحفظ اللحوم فإن:
</div>

$$A(r) = 2\pi rh + 2\pi r^2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالتعويض عن $h$ ينتج أن:
</div>

$$A(r) = (2\pi r) \left(\frac{1000}{r^2}\right) + (2\pi r^2)$$
$$= \frac{2000\pi}{r} + 2\pi r^2 \quad , \quad r > 0$$
$$A'(r) = \frac{-2000\pi}{r^2} + 4\pi r$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
المساحة السطحية للعلبة $A(r)$ أكبر ما يمكن عندما:
</div>

$$A'(r) = 0$$
$$\Rightarrow \frac{-2000\pi}{r^2} + 4\pi r = 0$$
$$\Rightarrow \frac{2000\pi}{r^2} = 4\pi r$$
$$\Rightarrow r^3 = 500$$
$$\Rightarrow r = 5\sqrt[3]{4} \text{ cm}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبالتعويض عن قيمة $(r)$ في المعادلة (3) ينتج أن:
</div>

$$h = \frac{1000}{(5\sqrt[3]{4})^2} = 10\sqrt[3]{4} \text{ cm}$$
$$A''(r) = \frac{4000\pi}{r^3} + 4\pi$$
$$A''(5\sqrt[3]{4}) = \frac{4000\pi}{500} + 4\pi$$
$$= 8\pi + 4\pi = 12\pi > 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ المساحة السطحية للعلبة المستعملة لحفظ اللحوم تكون أصغر ما يمكن عندما:
</div>

$$r = 5\sqrt[3]{4} \text{ cm} \quad , \quad h = 10\sqrt[3]{4} \text{ cm}$$

---

<div dir="rtl" style="text-align: left; font-size: 14px; font-weight: bold;">
الفصل 2 تطبيقات المشتقة &nbsp;&nbsp;&nbsp;&nbsp; 92
</div>
<!-- PAGE_END_92 -->


<!-- PAGE_START_93 -->
### صفحة 93

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4:</strong> إذا كانت العلاقة بين الإزاحة $s$ بالسنتيمترات، والزمن $t$ بالثواني لجسم متحرك في خط مستقيم هي $s(t) = t^3 - 9t^2 + 24t$ ، أوجد أقل سرعة لهذا الجسم.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
نرمز لسرعة الجسم بالرمز $v(t)$
</div>

$$ \because v(t) = s'(t) $$

$$ \therefore v(t) = 3t^2 - 18t + 24 $$

$$ v'(t) = 6t - 18 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
سرعة الجسم تكون أقل ما يمكن عندما:
</div>

$$ v'(t) = 0 $$

$$ \Rightarrow 6t - 18 = 0 $$

$$ \Rightarrow t = 3\text{ sec} $$

$$ v''(3) = 6 > 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
للدالة قيمة صغرى عندما $t = 3\text{ sec}$.<br>
$\therefore$ أقل سرعة للجسم هي:
</div>

$$ v(3) = 3(3)^2 - 18(3) + 24 $$

$$ = -3\text{ cm / sec} $$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الدرس 6-2 تطبيقات على القيم العظمى والصغرى</strong> <span style="float: left;"><strong>93</strong></span>
</div>
<!-- PAGE_END_93 -->


<!-- PAGE_START_94 -->
### صفحة 94

<div dir="rtl" style="text-align: right; font-size: 20px; font-weight: bold; margin-bottom: 20px;">
تمارين 2-6
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>1)</strong> أوجد العدد الموجب الذي مجموعه مع مقلوبه يكون أصغر ما يمكن.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>2)</strong> عددان موجبان مجموعهما 100، ومجموع مربعيهما أصغر ما يمكن، ما العددان؟
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>3)</strong> شُكِّل مستطيل من سلك طوله $20\text{ cm}$. احسب بعديه، بحيث تكون مساحة سطحه أكبر ما يمكن.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>4)</strong> مستطيل مساحة سطحه $900\text{ m}^2$. احسب بعديه، بحيث يكون محيطه أصغر ما يمكن.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>5)</strong> قطعة من الورق على شكل مربع طول ضلعه $30\text{ cm}$، قطع من أركانها الأربعة مربعات متساوية، ثم ثُنيت أضلاعها لتكوّن صندوقاً مفتوحاً. بيّن أن حجم الصندوق أكبر ما يمكن عندما يكون عمقه $5\text{ cm}$.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>6)</strong> يراد صنع وعاء على هيئة أسطوانة دائرية قائمة بغطاء سعتها $250\pi\text{ cm}^3$، أوجد أبعاد الوعاء التي تجعل مساحته السطحية أقل ما يمكن.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>7)</strong> نافذة على شكل مستطيل يعلوه نصف دائرة ، إذا كان محيط النافذة $9\text{ m}$، فأوجد الأبعاد التي تسمح بدخول أكبر كمية ممكنة من الضوء.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>8)</strong> عددان موجبان حاصل ضربهما 16، ما العددان إذا كان:
<br />
<strong>a)</strong> مجموعهما أقل ما يمكن.
<br />
<strong>b)</strong> مجموع أحدهما ومربع الآخر أقل ما يمكن.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>9)</strong> المثلث $ABC$ قائم الزاوية في $B$، إذا كان $AB + 2BC = 32\text{ cm}$، فأوجد أكبر مساحة للمثلث $ABC$.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>10)</strong> $ABCD$ مربع طول ضلعه $10\text{ cm}$، أُخذت النقطتان $M, N$ على $\overline{AB}, \overline{BC}$، بحيث كان $BM = NB$، أوجد موضعي النقطتين $M, N$، بحيث تكون مساحة الشكل $DNMC$ أكبر ما يمكن.
</div>

<hr style="border: 0.5px solid #eee; margin: 10px 0;" />

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>11)</strong> دائرة طول نصف قطرها $5\text{ cm}$، رسم داخلها المستطيل $ABCD$ ، بحيث تقع رؤوسه على الدائرة، أوجد أكبر مساحة لسطح هذا المستطيل.
</div>

<br />

<div dir="rtl" style="text-align: left; font-size: 14px; margin-top: 30px;">
<strong>94</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الفصل 2 تطبيقات المشتقة
</div>
<!-- PAGE_END_94 -->


<!-- PAGE_START_95 -->
### صفحة 95

<div dir="rtl" style="text-align: right; font-size: 16px;">
12- مخروط دائري قائم محيط قاعدته مضافًا إليه ارتفاعه يساوي $44\text{ cm}$. أوجد نصف قطر قاعدته عندما يكون حجمه أكبر ما يمكن. علمًا بأن حجم المخروط هو:
$$\left(V = \frac{1}{3} \pi r^2 h \quad , \quad \pi = \frac{22}{7}\right)$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
13- يتحرك جسم في خط مستقيم بحيث كانت العلاقة بين الإزاحة $s$ بالسنتيمترات، والزمن $t$ بالثواني هي $s(t) = t^3 - 9t^2 + 35t - 28$. أوجد سرعة الجسم وعجلته عند أي لحظة، ثم أوجد متى تكون سرعة الجسم أقل ما يمكن وقيمة هذه السرعة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
14- سلك طوله $56\text{ m}$، قطع السلك قطعتين، وعمل مربع من إحداهما، وعمل من القطعة الأخرى مستطيل النسبة بين بعديه $1 : 3$؛ احسب طول قطعتي السلك؛ لتكون مساحتا سطحي المربع والمستطيل أصغر ما يمكن.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
15- $ABCD$ مستطيل فيه $AB = 8\text{ cm} , BC = 12\text{ cm}$. أخذت النقطتان $H , K$ على $\overline{AB} , \overline{BC}$ على الترتيب، بحيث كان $BH + BK = 10\text{ cm}$. أوجد طول كل من $\overline{BH} , \overline{BK}$ الذي يجعل مساحة سطح الشكل $AHKCD$ أصغر ما يمكن.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
16- مثلث قائم الزاوية طول وتره $4\text{ cm}$، عين طولي ضلعي القائمة حتى تكون مساحة سطحه أكبر ما يمكن.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
17- $\triangle ABC$ متطابق الضلعين مرسوم داخل دائرة طول نصف قطرها $10\text{ cm}$، أنزل $AD$ عموديًا على $\overline{BC}$. أوجد طول $\overline{AD}$؛ لتصبح مساحة سطح المثلث أكبر ما يمكن.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
18- نافذة على شكل مستطيل مجموع طولي بعديه $6\text{ m}$، يعلوه مثلث قائم الزاوية متطابق الضلعين، وتره أحد بعدي المستطيل. أوجد بعدي المستطيل اللذين يسمحان بدخول أكبر كمية من الضوء.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 6-2 تطبيقات على القيم العظمى والصغرى | 95
</div>
<!-- PAGE_END_95 -->


<!-- PAGE_START_96 -->
### صفحة 96

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>اختبار الفصل 2</h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد ميل المماس لمنحنى كل دالة مما يأتي عند النقطة المعطاة:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
1) $f(x) = x^3 - 3x^2 + 7 , \quad (2, 3)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2) $f(x) = |x| , \quad x = 1 , \quad x = 0$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3) $f(x) = \sqrt{3x - 2} , \quad (2, 2)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
4) $f(x) = \frac{1+x}{1-x} , \quad (-1, 0)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
5) $y^2 + 2xy - 3x^2 = 0 , \quad (1, -3)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
6) $x^2 + y^2 + 2x - 8y + 12 = 0 , \quad (1, 5)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
7) أوجد النقاط الواقعة على منحنى الدالة $y = \sqrt{x^2 - 4}$ التي يكون عندها المماس رأسياً.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
8) أوجد النقاط الواقعة على منحنى الدالة $y = x^3 - 7x$ التي يصنع المماس عندها زاوية قياسها $\frac{3\pi}{4}$ مع الاتجاه الموجب للمحور $x$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
9) أوجد معادلة المماس لمنحنى الدالة $y = \frac{9x}{1-x^2} , \quad x \neq \pm 1$ عند النقطة $(2, -6)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
10) أثبت أن النقطة $(3, -1)$ تقع على منحنى $x^2 + y^2 - 4x + 2y = 20$، ثم أوجد معادلة المماس والعمودي للمنحنى عندها.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
11) أوجد معادلة العمودي لمنحنى $y + \sqrt{x} = 12$ عند نقاط تقاطعه مع المستقيم $x = y$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
12) يتحرك جسم في خط مستقيم وفقاً للعلاقة: $s = t^3 - 9t^2 + 15t$، حيث الإزاحة $s$ بالأمتار، والزمن $t$ بالثواني. أوجد سرعة هذا الجسم، وتسارعه عند أي لحظة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
13) يتحرك جسم في خط مستقيم، بحيث تكون العلاقة بين الإزاحة $s$ بالسنتيمترات، والزمن $t$ بالثواني هي $s = \cos 2t + \sin 2t$. أثبت أن $s'' = -4s$ (عددياً).
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
14) يتحرك جسم في خط مستقيم مبتدأً من نقطة ثابتة وفقاً للعلاقة $s = 8\sin^2 t$، حيث $s$ بُعد الجسم عن النقطة الثابتة بالسنتيمترات بعد مضي $t$ بالثواني. أوجد تسارع الجسم بعد مضي $\frac{\pi}{2} \text{ sec}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
15) صفيحة مستوية من المعدن مستطيلة الشكل قياس طولها يساوي مثلي قياس عرضها تتمدد بالحرارة. أوجد معدل التغير في قياس محيطها. إذا كان معدل تغير قياس طولها يساوي $0.02 \text{ cm/sec}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
16) أوجد إحداثيات النقاط التي تقع على المنحنى $y^2 + x^2 = 8$ والتي يكون عندها معدل تغير الإحداثي $y$ لها بالنسبة للزمن يساوي معدل تغير الإحداثي $x$ بالنسبة للزمن.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
17) يتحرك رجل نحو قاعدة برج بمعدل $1 \text{ m/sec}$. إذا كان ارتفاع البرج $9 \text{ m}$، فأوجد معدل اقتراب الرجل من قمة البرج، عندما يكون على بُعد $12 \text{ m}$ من قاعدته.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
18) مكعب يتمدد بالحرارة فيزداد طول حرفه بمعدل $0.08 \text{ cm/min}$. أوجد معدل تغير المساحة الكلية له في اللحظة التي يكون فيها معدل تغير الحجم مساوياً $0.96 \text{ cm}^3/\text{min}$ (علماً بأن حجم المكعب هو $V = l^3$).
</div>
<!-- PAGE_END_96 -->
