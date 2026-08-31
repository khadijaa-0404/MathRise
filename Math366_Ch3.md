

<!-- PAGE_START_100 -->
### صفحة 100

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1>3-1 العلاقة بين التفاضل والتكامل</h1>
<h3>The Relation Between Differentiation and Integration</h3>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
سندرس فيما يأتي العلاقة بين التفاضل والتكامل، وهذا ليس للأهمية من الناحية النظرية للموضوع فحسب، بل لأن هذه العلاقة ستكشف وسائل أكثر سهولة؛ لحساب كثير من التكاملات.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
تعلم أنه في عملية التفاضل يكون لدينا دالة ولتكن $F$، ثم نوجد مشتقتها عند نقطة ما، أو في فترة ما مثل $[a, b]$ إن كان لهذه المشتقة وجود. وسنهتم الآن بعكس هذه العملية، حيث يكون لدينا دالة $f$ نعلم أنها الدالة المشتقة لدالة ما $F$ في الفترة $[a, b]$، ويكون هدفنا هو إيجاد الدالة $F$، أي أننا سنهتم بالمشكلة الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذا كانت الدالة $f$ معرفة على الفترة $[a, b]$، فما هي الدالة $F$، بحيث يكون
</div>

$$F'(x) = f(x) \quad \forall x \in (a, b)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
إن مثل هذه الدالة $F$ إن وجدت تسمى <b>بالدالة الأصلية</b> أو <b>عكس المشتقة</b> للدالة $f$ في الفترة $[a, b]$، والدالة الأصلية $F$ ينبغي أن يتوفر فيها ما يأتي:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #ccc; padding: 15px; border-radius: 8px; background-color: #f9f9f9;">
<strong>تعريف</strong>
<br><br>
يقال للدالة $F$ إنها دالة أصلية أو عكس المشتقة للدالة $f$ في الفترة $[a, b]$، إذا كانت $F$ متصلة في الفترة $[a, b]$، وقابلة للاشتقاق في الفترة $(a, b)$. وكان
$$F'(x) = f(x) \quad \forall x \in (a, b)$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أي أنه لإيجاد الدالة $F$ نبحث عن الدالة التي إذا فضلت تعطي الدالة $f$، ونعتمد في بحثنا هذا على معلوماتنا في التفاضل، وعلى النظرية الآتية التي سنقدمها هنا دون برهان.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #ccc; padding: 15px; border-radius: 8px; background-color: #eef9f5;">
<strong>نظرية</strong>
<br><br>
لكل دالة متصلة في فترة مغلقة دالة أصلية في هذه الفترة.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px; color: #555;">
الفصل 3 التكامل غير المحدد | 100
</div>
<!-- PAGE_END_100 -->


<!-- PAGE_START_101 -->
### صفحة 101

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1</strong><br>
إذا كانت $F(x) = x^2$ ، $f(x) = 2x$ ، فأثبت أن الدالة $F$ دالة أصلية للدالة $f$ في $\mathbb{R}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
$\because$ الدالة $F$ متصلة في $\mathbb{R}$ (لماذا؟)
</div>

$$F'(x) = 2x = f(x) \quad \forall x \in \mathbb{R}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ الدالة $F$ دالة أصلية للدالة $f$ في $\mathbb{R}$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
ونلاحظ أن الدالة $F$ ليست الدالة الأصلية الوحيدة للدالة $f$ ، بل يوجد عدد لا نهائي من الدوال الأصلية للدالة $f(x)$ فمثلاً:
</div>

$$F_1(x) = x^2 + 1 \quad \forall x \in \mathbb{R} ,$$

$$F_2(x) = x^2 - 3 \quad \forall x \in \mathbb{R} ,$$

$$F_3(x) = x^2 + \frac{1}{2} \quad \forall x \in \mathbb{R} ,$$

$$F_4(x) = x^2 - \sqrt{2} \quad \forall x \in \mathbb{R}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
جميعها دوال أصلية للدالة $f$ ، وكل دالة من هذه الدوال متصلة في $\mathbb{R}$ حيث
</div>

$$F'_1(x) = F'_2(x) = F'_3(x) = F'_4(x) = f(x)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وكل من هذه الدوال الأصلية لا تختلف عن أي دالة أصلية أخرى إلا في قيمة الحد المطلق.

وكل دالة أصلية تأخذ الصورة $(x^2 + C)$ حيث $C$ عدد ثابت، ويرمز لمجموعة الدوال الأصلية للدالة $f$ بالرمز $F(x) + C$ ، حيث $C \in \mathbb{R}$.

وبصفة عامة إذا كان للدالة ما $f(x)$ دالة أصلية $F(x)$ فإن يوجد عدد لانهائي من الدوال الأصلية للدالة $f$ ، وتأخذ كل منها الصورة $(F(x) + C)$ ، حيث $C$ عدد ثابت، ويرمز لمجموعة الدوال الأصلية للدالة $f$ بالرمز $(F(x) + C)$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>101</strong> | الدرس 1-3 العلاقة بين التفاضل والتكامل
</div>
<!-- PAGE_END_101 -->


<!-- PAGE_START_102 -->
### صفحة 102

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2)</strong>
<br>
أوجد مجموعة الدوال الأصلية لكل دالة مما يأتي في الفترة المعطاة:
</div>

$$a) \quad f(x) = 3x^2 \quad , \quad x \in \mathbb{R}$$

$$b) \quad f(x) = \cos x \quad , \quad x \in \left[0, \frac{\pi}{2}\right]$$

$$c) \quad f(x) = \sec^2 x \quad , \quad x \in \left[0, \frac{\pi}{3}\right]$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>a)</strong>
</div>

$$F(x) = x^3$$

$$\because F(x) \text{ متصلة في } \mathbb{R} , \quad F'(x) = 3x^2 = f(x) \quad \forall x \in \mathbb{R}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ الدالة $F$ دالة أصلية للدالة $f$ ، ومنه مجموعة الدوال الأصلية للدالة $f$ هي:
</div>

$$F(x) + c = x^3 + c$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>b)</strong>
</div>

$$F(x) = \sin x$$

$$\because F(x) \text{ متصلة في الفترة } \left[0, \frac{\pi}{2}\right] , \quad F'(x) = \cos x = f(x) \quad \forall x \in \left(0, \frac{\pi}{2}\right)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ الدالة $F$ دالة أصلية للدالة $f$ ، ومنه مجموعة الدوال الأصلية للدالة $f$ هي:
</div>

$$F(x) + c = \sin x + c$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>c)</strong>
</div>

$$F(x) = \tan x$$

$$\because F(x) \text{ متصلة في الفترة } \left[0, \frac{\pi}{3}\right] , \quad F'(x) = \sec^2 x = f(x) \quad \forall x \in \left(0, \frac{\pi}{3}\right)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ الدالة $F$ دالة أصلية للدالة $f$ ، ومنه مجموعة الدوال الأصلية للدالة $f$ هي:
</div>

$$F(x) + C = \tan x + C$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب</strong>
<br>
أوجد مجموعة الدوال الأصلية لكل دالة مما يأتي في الفترة المعطاة:
</div>

$$a) \quad f(x) = 6x^2 , \quad x \in \mathbb{R}$$

$$b) \quad f(x) = x + 1 , \quad x \in \mathbb{R}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 3: التكامل غير المحدد | 102
</div>
<!-- PAGE_END_102 -->


<!-- PAGE_START_103 -->
### صفحة 103

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1>3-2 التكامل غير المحدد</h1>
<p><em>Indefinite Integral</em></p>
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تعريف</strong>
<h3>مشتقة دالة</h3>
إذا كانت كل من $f(x)$ ، $F(x)$ متصلة في الفترة $[a, b]$ ، وكان $F'(x) = f(x)$ ، فإن 
مجموعة الدوال الأصلية $(F(x) + C, C \in \mathbb{R})$ تسمى 
<strong>التكامل غير المحدد للدالة $f$</strong> ، ويرمز له بالرمز $\int f(x) \, dx$ ، أي أن :
</div>

$$\int f(x) \, dx = F(x) + C, \quad C \in \mathbb{R}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويسمى $C$ ثابت التكامل غير المحدد.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
من هذا التعريف يتضح أنه للحصول على $f(x)$ ، فإننا نشتق $F(x)$ بالنسبة للمتغير $x$ ، 
وبالعكس للحصول على $F(x)$ ، فإننا نكامل $f(x)$ بالنسبة للمتغير $x$ ، أي أن التكامل عملية 
عكسية للإشتقاق، ويتضح ذلك من الأمثلة المبينة في الجدول أدناه.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">

| التكامل غير المحدد | المشتقة |
| :---: | :---: |
| $\int 5x^4 \, dx = x^5 + C$ | $\frac{d}{dx}(x^5) = 5x^4$ |
| $\int \sec x \tan x \, dx = \sec x + C$ | $\frac{d}{dx}(\sec x) = \sec x \tan x$ |
| $\int \cos x \, dx = \sin x + C$ | $\frac{d}{dx}(\sin x) = \cos x$ |
| $\int \frac{1}{2\sqrt{x}} \, dx = \sqrt{x} + C$ | $\frac{d}{dx}(\sqrt{x}) = \frac{1}{2\sqrt{x}}$ |

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 2-3 التكامل غير المحدد | 103
</div>
<!-- PAGE_END_103 -->


<!-- PAGE_START_104 -->
### صفحة 104

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>نتيجة:</b><br>
إذا كانت $f(x) = kx^n$ متصلة في الفترة $[a, b]$، فإن:
</div>

$$\int kx^n \, dx = \frac{k}{n+1} x^{n+1} + C, \quad n, k, C \in \mathbb{R}, \; n \neq -1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>البرهان:</b><br>
$\because f(x) = kx^n$<br>
$\because f(x)$ متصلة في الفترة $[a, b]$<br>
إذن $F(x) = \frac{k}{n+1} x^{n+1}$ متصلة في الفترة $[a, b]$<br>
$\because F'(x) = \frac{k}{n+1}(n+1)x^n = kx^n = f(x)$<br>
$\therefore$ الدالة $F$ دالة أصلية للدالة $f$ ومنه:
</div>

$$\int kx^n \, dx = \frac{k}{n+1} x^{n+1} + C$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال (1):</b><br>
أوجد كلاً من التكاملات الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $\int 3x^6 \, dx$<br>
b) $\int 8 \, dx$<br>
c) $\int 4x^{-5} \, dx$<br>
d) $\int \sqrt{x} \, dx$<br>
e) $\int 7x^{\frac{4}{3}} \, dx$<br>
f) $\int x^{-\frac{2}{5}} \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل:</b>
</div>

$$\text{a) } \int 3x^6 \, dx = \frac{3x^7}{7} + C$$

$$\text{b) } \int 8 \, dx = 8x + C$$

$$\text{c) } \int 4x^{-5} \, dx = \frac{4x^{-4}}{-4} + C = -x^{-4} + C, \quad x \neq 0$$

$$\text{d) } \int \sqrt{x} \, dx = \int x^{\frac{1}{2}} \, dx = \frac{2}{3} x^{\frac{3}{2}} + C, \quad x \geq 0$$

$$\text{e) } \int 7x^{\frac{4}{3}} \, dx = \frac{7x^{\frac{7}{3}}}{\frac{7}{3}} + C = 3x^{\frac{7}{3}} + C$$

$$\text{f) } \int 3x^{-\frac{2}{5}} \, dx = \frac{5}{3} x^{\frac{3}{5}} + C$$

---
<div dir="rtl" style="text-align: right; font-size: 14px; color: gray;">
الفصل 3: التكامل غير المحدد | 104
</div>
<!-- PAGE_END_104 -->


<!-- PAGE_START_105 -->
### صفحة 105

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نتيجة (2)</strong>
<br>
إذا كانت $f(x)$ قابلة للاشتقاق في الفترة $(a, b)$، فإن:
</div>

$$\int (f(x))^n f'(x) \, dx = \frac{1}{n+1} (f(x))^{n+1} + C, \quad n, C \in \mathbb{R}, \; n \neq -1$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان:</strong>
<br>
$\because \frac{d}{dx} \left[ \frac{1}{n+1} (f(x))^{n+1} + C \right] = \frac{1}{n+1} (n+1) (f(x))^n f'(x) = (f(x))^n f'(x)$
<br>
$\therefore$ الدالة $\frac{1}{n+1} (f(x))^{n+1}$ دالة أصلية للدالة $(f(x))^n f'(x)$ ومنه:
</div>

$$\int (f(x))^n f'(x) \, dx = \frac{1}{1+n} (f(x))^{n+1} + C$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2)</strong>
<br>
أوجد كلّاً من التكاملات الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $\int 5(5x + 1)^3 \, dx$
<br>
b) $\int 2u(u^2 + 3)^4 \, du$
<br>
c) $\int 3x^2 \sqrt{x^3 - 1} \, dx$
<br>
d) $\int (2x - 1)(x^2 - x + 4)^{-2} \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$a) \quad \int 5(5x + 1)^3 \, dx = \frac{1}{4}(5x + 1)^4 + C$$

$$b) \quad \int 2u(u^2 + 3)^4 \, du = \frac{1}{5}(u^2 + 3)^5 + C$$

$$c) \quad \int 3x^2 \sqrt{x^3 - 1} \, dx = \frac{(x^3 - 1)^{\frac{3}{2}}}{\frac{3}{2}} + C = \frac{2}{3} (\sqrt{x^3 - 1})^3 + C$$

$$d) \quad \int (2x - 1)(x^2 - x + 4)^{-2} \, dx = \frac{(x^2 - x + 4)^{-1}}{-1} + C = \frac{-1}{x^2 - x + 4} + C$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (3)</strong>
<br>
أوجد كلّاً من التكاملات الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $\int \sin^5 x \cos x \, dx$
<br>
b) $\int \csc^4 x \cot x \, dx$
<br>
c) $\int \sin \theta \cos \theta \, d\theta$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$a) \quad \int \sin^5 x \cos x \, dx = \frac{1}{6} \sin^6 x + C$$

$$b) \quad \int \csc^4 x \cot x \, dx = \int \csc^3 x (\csc x \cot x) \, dx = -\frac{1}{4} \csc^4 x + C$$

$$c) \quad \int \sin \theta \cos \theta \, d\theta = \frac{1}{2} \sin^2 \theta + C$$

<div dir="rtl" style="text-align: center; font-size: 16px;">
أو
</div>

$$\int \sin \theta \cos \theta \, d\theta = -\frac{1}{2} \cos^2 \theta + C$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 3-2: التكامل غير المحدد | 105
</div>
<!-- PAGE_END_105 -->


<!-- PAGE_START_106 -->
### صفحة 106

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>تدريب</b><br>
أوجد كلًّا من التكاملات الآتية:
</div>

$$\text{a) } \int 2z (z^2 + 4)^8 \, dz$$

$$\text{b) } \int \frac{2x}{\sqrt{x^2 + 8}} \, dx$$

$$\text{c) } \int \sqrt{\tan x} \sec^2 x \, dx$$

$$\text{d) } \int \sec^3 x \tan x \, dx$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>ملخص المفهوم: التكاملات غير المحددة لبعض الدوال الأساسية</b>
</div>

$$\int k \, dx = kx + C \quad, C \in \mathbb{R}$$

$$\int k x^n \, dx = \frac{k}{n+1} x^{n+1} + C \quad, n, k \in \mathbb{R}, n \neq -1$$

$$\int \cos x \, dx = \sin x + C$$

$$\int \sin x \, dx = -\cos x + C$$

$$\int \sec^2 x \, dx = \tan x + C$$

$$\int \csc^2 x \, dx = -\cot x + C$$

$$\int \sec x \tan x \, dx = \sec x + C$$

$$\int \csc x \cot x \, dx = -\csc x + C$$

$$\int \cos kx \, dx = \frac{1}{k} \sin kx + C \quad, k \neq 0$$

$$\int \sin kx \, dx = -\frac{1}{k} \cos kx + C \quad, k \neq 0$$

$$\int (f(x))^n f'(x) \, dx = \frac{1}{n+1} (f(x))^{n+1} + C \quad, n \neq -1$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>نظرية</b><br>
إذا كانت للدالة $f$ دالة أصلية في فترة ما $[a, b]$، وكان $k$ عددًا حقيقيًّا، فإن للدالة $(kf)$ دالة أصلية في هذه الفترة كما أن:
</div>

$$\int (kf)(x) \, dx = k \int f(x) \, dx$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>106</b> الفصل 3: التكامل غير المحدد
</div>
<!-- PAGE_END_106 -->


<!-- PAGE_START_107 -->
### صفحة 107

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان:</strong><br>
لتكن الدالة $F$ دالة أصلية للدالة $f$ في الفترة $[a, b]$<br>
$\because (kF)'(x) = kF'(x) = k f(x)$<br>
$\therefore$ الدالة $(kF)$ دالة أصلية للدالة $k f$ ومنه:
</div>

$$ \int k f(x) \, dx = kF + c_1, \quad c_1 \in \mathbb{R} $$
$$ = k(F + c) $$
$$ = k \int f(x) \, dx $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4</strong><br>
أوجد كلًّا من التكاملات الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $\int 6 \cos^2 x \sin x \, dx$<br>
b) $\int 8x^3 (x^4 + 1)^6 \, dx$<br>
c) $\int \frac{-6x}{\sqrt{1 - x^2}} \, dx$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>(a</strong>
</div>

$$ \int 6 \cos^2 x \sin x \, dx = 6 \int \cos^2 x \sin x \, dx $$
$$ = 6 \left(-\frac{1}{3}\right) \cos^3 x + C $$
$$ = -2 \cos^3 x + C $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>(b</strong>
</div>

$$ \int 8x^3 (x^4 + 1)^6 \, dx = 2 \int 4x^3 (x^4 + 1)^6 \, dx $$
$$ = 2 \left(\frac{1}{7}\right) (x^4 + 1)^7 + C $$
$$ = \frac{2}{7} (x^4 + 1)^7 + C $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>(c</strong>
</div>

$$ \int \frac{-6x}{\sqrt{1 - x^2}} \, dx = 3 \int \frac{-2x}{\sqrt{1 - x^2}} \, dx $$
$$ = 3 \int -2x (1 - x^2)^{-\frac{1}{2}} \, dx $$
$$ = 3 (2) (1 - x^2)^{\frac{1}{2}} + C $$
$$ = 6 \sqrt{1 - x^2} + C $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>107</strong> | الدرس 3-2 التكامل غير المحدد
</div>
<!-- PAGE_END_107 -->


<!-- PAGE_START_108 -->
### صفحة 108

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>نظرية</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذا كان كل من الدالة $f_1 , f_2$ دالة أصلية في فترة ما $[a, b]$، فإن الدالة $(f_1 \pm f_2)$ دالة أصلية في هذه الفترة كما أن:
</div>

$$\int (f_1 \pm f_2)(x) \, dx = \int f_1(x) \, dx \pm \int f_2(x) \, dx$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>البرهان</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
لتكن $F_1(x) , F_2(x)$ دالتين أصليتين لـ $f_1(x) , f_2(x)$ على الترتيب في الفترة $[a, b]$،
</div>

$$\because (F_1 \pm F_2)'(x) = F_1'(x) \pm F_2'(x)$$
$$= f_1(x) \pm f_2(x)$$
$$= (f_1 \pm f_2)(x)$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ الدالة $(F_1 \pm F_2)(x)$ دالة أصلية للدالة $(f_1 \pm f_2)(x)$.
</div>

$$\therefore \int (f_1 + f_2)(x) \, dx = (F_1 \pm F_2)(x) + C$$
$$= (F_1(x) + C_1) \pm (F_2(x) + C_2)$$
$$= \int f_1(x) \, dx \pm \int f_2(x) \, dx$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
وتُعمم هذه الخاصية لأي عدد محدد من الدوال الحقيقية. فمثلاً:
</div>

$$\int (x^2 - 8x + 5) \, dx = \int x^2 \, dx - \int 8x \, dx + \int 5 \, dx$$
$$= \frac{x^3}{3} + C_1 - \frac{8x^2}{2} + C_2 + 5x + C_3$$
$$= \frac{1}{3}x^3 - 4x^2 + 5x + (C_1 + C_2 + C_3)$$
$$= \frac{1}{3}x^3 - 4x^2 + 5x + C$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ويمكن إيجاد التكامل مباشرة كالأتي:
</div>

$$\int (x^2 - 8x + 5) \, dx = \frac{1}{3}x^3 - 4x^2 + 5x + C$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الفصل 3:</strong> التكامل غير المحدد | 108
</div>
<!-- PAGE_END_108 -->


<!-- PAGE_START_109 -->
### صفحة 109

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (5)</strong>
<br>
أوجد كلاً من التكاملات الآتية:
</div>

$$a) \quad \int (4x^3 + 6x^2 - 9x) \, dx$$

$$b) \quad \int (x - 1)(x + 5) \, dx$$

$$c) \quad \int (x^2 + 1)^2 \, dx$$

$$d) \quad \int \frac{t^2 - 8t + 15}{t - 3} \, dt, \quad t \neq 3$$

$$e) \quad \int \frac{x^5 + 4}{x^3} \, dx, \quad x \neq 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\text{(a)} \quad \int (4x^3 + 6x^2 - 9x) \, dx = \frac{4x^4}{4} + \frac{6x^3}{3} - \frac{9x^2}{2} + C$$

$$= x^4 + 2x^3 - \frac{9}{2}x^2 + C$$

$$\text{(b)} \quad \int (x - 1)(x + 5) \, dx = \int (x^2 + 4x - 5) \, dx$$

$$= \frac{1}{3}x^3 + 2x^2 - 5x + C$$

$$\text{(c)} \quad \int (x^2 + 1)^2 \, dx = \int (x^4 + 2x^2 + 1) \, dx$$

$$= \frac{1}{5}x^5 + \frac{2}{3}x^3 + x + C$$

$$\text{(d)} \quad \int \frac{t^2 - 8t + 15}{t - 3} \, dt = \int \frac{(t - 3)(t - 5)}{t - 3} \, dt, \quad t \neq 3$$

$$= \int (t - 5) \, dt$$

$$= \frac{1}{2}t^2 - 5t + C$$

$$\text{(e)} \quad \int \frac{x^5 + 4}{x^3} \, dx = \int \left( \frac{x^5}{x^3} + \frac{4}{x^3} \right) \, dx, \quad x \neq 0$$

$$= \int (x^2 + 4x^{-3}) \, dx$$

$$= \frac{1}{3}x^3 + \frac{4x^{-2}}{-2} + C$$

$$= \frac{1}{3}x^3 - \frac{2}{x^2} + C$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>109</strong> | الدرس 3-2: التكامل غير المحدد
</div>
<!-- PAGE_END_109 -->


<!-- PAGE_START_110 -->
### صفحة 110

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 6</b><br>
أوجد كُلاً من التكاملات الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $\int \left(\frac{1 + \sin x}{\cos^2 x}\right) dx$
<br>
b) $\int \sin^2 x \, dx$
<br>
c) $\int \cos^3 x \, dx$
<br>
d) $\int \cot^2 \theta \, d\theta$
<br>
e) $\int \sec^4 x \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل:</b>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>a)</b>
</div>
$$\int \left(\frac{1 + \sin x}{\cos^2 x}\right) dx = \int \left(\frac{1}{\cos^2 x} + \frac{\sin x}{\cos^2 x}\right) dx$$
$$= \int (\sec^2 x + \tan x \sec x) dx$$
$$= \tan x + \sec x + C$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>b)</b>
</div>
$$\int \sin^2 x \, dx = \int \frac{1}{2} (1 - \cos 2x) \, dx$$
$$= \frac{1}{2} \left(x - \frac{1}{2} \sin 2x\right) + C$$
$$= \frac{1}{2} x - \frac{1}{4} \sin 2x + C$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>c)</b>
</div>
$$\int \cos^3 x \, dx = \int [\cos x (\cos^2 x)] dx$$
$$= \int [\cos x (1 - \sin^2 x)] dx$$
$$= \int (\cos x - \sin^2 x \cos x) dx$$
$$= \sin x - \frac{1}{3} \sin^3 x + C$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>d)</b>
</div>
$$\int \cot^2 \theta \, d\theta = \int (\csc^2 \theta - 1) \, d\theta$$
$$= -\cot \theta - \theta + C$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>e)</b>
</div>
$$\int \sec^4 x \, dx = \int [(\sec^2 x)(\sec^2 x)] dx$$
$$= \int [(\sec^2 x)(1 + \tan^2 x)] dx$$
$$= \int (\sec^2 x + \sec^2 x \tan^2 x) dx$$
$$= \tan x + \frac{1}{3} \tan^3 x + C$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الفصل 3: التكامل غير المحدد | 110
</div>
<!-- PAGE_END_110 -->


<!-- PAGE_START_111 -->
### صفحة 111

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين 2-3</h2>

<p>أوجد كلاً من التكاملات الآتية:</p>

1) $\int (5x^4 + 3x^2 - 4x + 7) \, dx$

2) $\int (x - 2)(x^2 + 1) \, dx$

3) $\int x^3 (3x + 4) \, dx$

4) $\int \frac{1}{x^4} (x^2 + x^5) \, dx$

5) $\int \sqrt{x} \, dx$

6) $\int \sqrt{x} (x + 2) \, dx$

7) $\int \sqrt[3]{x - 2} \, dx$

8) $\int \sqrt{3x + 1} \, dx$

9) $\int \frac{x^2 - 7x - 18}{x + 2} \, dx$

10) $\int x (x^2 + 12)^3 \, dx$

11) $\int (x + 7) \sqrt{x^2 + 14x - 1} \, dx$

12) $\int \frac{-2}{\sqrt{1 - 2x}} \, dx$

13) $\int x^3 (x^4 + 1)^6 \, dx$

14) $\int 15 x^2 \sqrt[5]{x^3 + 7} \, dx$

15) $\int \frac{2x - 3}{(x^2 - 3x + 1)^5} \, dx$

16) $\int \sin 3u \, du$

17) $\int (2\cos^2 x - 1) \, dx$

18) $\int \cot^4 x \csc^2 x \, dx$

19) $\int \cos x \sqrt[3]{\sin x - 5} \, dx$

20) $\int \sin x (1 - \sin^2 x) \, dx$

21) $\int \tan^2 x \, dx$

22) $\int (\tan^3 x + \tan x) \, dx$

23) $\int 5 \tan x \cot x \, dx$

24) $\int (\sin x + \cos x)^2 \, dx$

25) $\int \sin^3 2x \cos 2x \, dx$

26) $\int \frac{\cot x}{\sin x} \, dx$

</div>

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>111</b> الدرس 2-3 التكامل غير المحدد
</div>
<!-- PAGE_END_111 -->


<!-- PAGE_START_112 -->
### صفحة 112

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1>3-3 تطبيقات على التكامل غير المحدد</h1>
<p><strong>Applications of Indefinite Integral</strong></p>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: #c00000;">تطبيقات هندسية</h3>
<p>
رأينا فيما سبق أنه لإيجاد ميل المماس لمنحنى $y = f(x)$ عند أي نقطة $(x, y)$ تقع على المنحنى ، فإننا نوجد المشتقة الأولى $f'(x)$ عند تلك النقطة، وحيث إن التكامل عملية عكسية للاشتقاق؛ لذا فإننا يمكننا إيجاد معادلة المنحنى إذا عُلِمَ ميل المماس له عند أي نقطة $(x, y)$ واقعة عليه.
</p>
</div>

<br>

<div dir="rtl" style="text-align: center; font-size: 16px;">
$$y = f(x) \xrightarrow{\text{بالاشتقاق بالنسبة للمتغير } x} y' = f'(x)$$
<p>ميل المماس $m$ لمنحنى الدالة $y = f(x)$ عند النقطة $(x, y)$ الواقعة عليه</p>
$$y = \int f'(x) \, dx = \int \frac{dy}{dx} \, dx \xleftarrow{\text{بالتكامل بالنسبة للمتغير } x}$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #00a0e9; padding: 10px; background-color: #f9f9f9;">
<strong style="background-color: #00a0e9; color: white; padding: 3px 8px; float: left;">مثال 1</strong>
<p>
إذا كان ميل المماس $m$ لمنحنى $y = f(x)$ عند أي نقطة $(x, y)$ واقعة عليه يُعطى بالعلاقة $m = f'(x) = 2x - 4$ ، فأوجد معادلة هذا المنحنى، علماً بأنه يمر بالنقطة $(2, -1)$ .
</p>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h4 style="color: #00a0e9;">الحل</h4>
</div>

$$\because y = \int f'(x) \, dx \quad , \quad m = f'(x) = 2x - 4$$

$$\therefore y = \int (2x - 4) \, dx$$

$$y = x^2 - 4x + C$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p>
وهذه المعادلة تُمثل مجموعة من المنحنيات التي ميل المماس لها عند أي نقطة $(x, y)$ واقعة عليها هو $2x - 4$، والنقطة $(2, -1)$ تُحدد معادلة المنحنى المطلوب، حيث
</p>
</div>

<br>

<hr>
<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>112</strong> | الفصل 3: التكامل غير المحدد
</div>
<!-- PAGE_END_112 -->


<!-- PAGE_START_113 -->
### صفحة 113

<div dir="rtl" style="text-align: right; font-size: 16px;">
النقطة $(-1, 2)$ تقع على منحنى هذه الدالة؛ إذن النقطة $(-1, 2)$ تحقق معادلته.
</div>

$$ -1 = 4 - 8 + C $$
$$ C = 3 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذن معادلة المنحنى المطلوب هي $y = x^2 - 4x + 3$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2):</strong><br>
إذا كان ميل المماس لمنحنى $y = f(x)$ عند أي نقطة $(x, y)$ واقعة عليه يعطى بالعلاقة: $m = \frac{dy}{dx} = 3x^2 + k , \quad k \in \mathbb{R}$ ، فأوجد معادلة هذا المنحنى علمًا بأنه يمر بالنقطتين $(-3, 2) , (0, 5)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because y = \int \frac{dy}{dx} \, dx \quad , \quad m = \frac{dy}{dx} = 3x^2 + k , \quad k \in \mathbb{R} $$

$$ \therefore y = \int (3x^2 + k) \, dx $$

$$ y = x^3 + kx + C \quad \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots (1) $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
بما أن النقطة $(-3, 2)$ تقع على منحنى هذه الدالة؛ إذن النقطة $(-3, 2)$ تحقق المعادلة (1).
</div>

$$ \therefore 2 = (-3)^3 - 3k + C $$

$$ C - 3k - 29 = 0 \quad \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots (2) $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
كذلك النقطة $(0, 5)$ تحقق المعادلة (1)
</div>

$$ \therefore 5 = 0 + 0 + C $$
$$ C = 5 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
بالتعويض عن قيمة $C$ في المعادلة (2)
</div>

$$ \therefore 5 - 3k - 29 = 0 $$
$$ k = -8 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذن معادلة المنحنى المطلوب هي $y = x^3 - 8x + 5$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>113</strong> | الدرس 3-3 تطبيقات على التكامل غير المحدد
</div>
<!-- PAGE_END_113 -->


<!-- PAGE_START_114 -->
### صفحة 114

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3:</strong><br>
أوجد معادلة المنحنى الذي ميل مماسه عند أي نقطة $(x, y)$ واقعة عليه يُعطى بالعلاقة:
</div>

$$ m = \frac{dy}{dx} = 3\sin^2 x \cos x $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
علمًا بأنه يمر بالنقطة $\left(\frac{\pi}{6}, 0\right)$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because y = \int \frac{dy}{dx} \, dx \quad , \quad m = \frac{dy}{dx} = 3\sin^2 x \cos x $$

$$ \therefore y = \int (3\sin^2 x \cos x) \, dx $$

$$ = \sin^3 x + C $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وحيث إن المنحنى المطلوب إيجاد معادلته يمر بالنقطة $\left(\frac{\pi}{6}, 0\right)$
</div>

$$ \therefore 0 = \sin^3 \frac{\pi}{6} + C $$

$$ 0 = \frac{1}{8} + C $$

$$ C = -\frac{1}{8} $$

$$ \therefore y = \sin^3 x - \frac{1}{8} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب:</strong><br>
أوجد معادلة المنحنى الذي ميل المماس $m$ عند أي نقطة واقعة عليه يُعطى بالعلاقة: $m = f'(x) = 3x^2 - 8x + 5$ ، علمًا بأنه يمر بالنقطة $(-1, 9)$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4:</strong><br>
دالة مشتقتها الأولى $\frac{dy}{dx} = 2x - 6$ ، وقيمتها الصغرى المحلية تساوي $(-4)$ ، أوجد هذه الدالة.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
بما أنه عند القيمة الصغرى المحلية للدالة يكون:
</div>

$$ \frac{dy}{dx} = 0 $$

$$ 2x - 6 = 0 $$

$$ x = 3 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذن النقطة الصغرى المحلية هي $(3, -4)$.
</div>

$$ \because \frac{dy}{dx} = 2x - 6 $$

$$ \therefore y = \int \frac{dy}{dx} \, dx = \int (2x - 6) \, dx $$

$$ y = x^2 - 6x + C $$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>114</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>الفصل 3: التكامل غير المحدد</strong>
</div>
<!-- PAGE_END_114 -->


<!-- PAGE_START_115 -->
### صفحة 115

<div dir="rtl" style="text-align: right; font-size: 16px;">
بما أن للدالة نقطة صغرى محلية عند $(3, -4)$؛ إذن المنحنى يمر بالنقطة $(3, -4)$.
</div>

$$ -4 = 9 - 18 + C $$
$$ C = 5 $$
$$ \therefore y = x^2 - 6x + 5 $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>تطبيقات فيزيائية</h3>

درست في تطبيقات المشتقة أنه إذا تحرك جسم في خط مستقيم، وكانت إزاحته عن نقطة ثابتة $O$ بعد زمن قدره $t$ ثانية هي $s$ بالسنتيمترات، فإن سرعته $v$ بالسنتيمتر لكل ثانية تُعطى بالعلاقة:
</div>

$$ v = \frac{ds}{dt} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
كذلك إذا عُلِمَت أن سرعة الجسم $v$ بعد زمن قدره $t$ ، فإن تسارع الجسم $a$ بالسنتيمتر لكل ثانية مربعة يُعطى بالعلاقة:
</div>

$$ a = \frac{dv}{dt} = \frac{d^2s}{dt^2} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وحيث إن التكامل عملية عكسية للاشتقاق، فإنه يمكن إيجاد إزاحة جسم متحرك إذا عُلِمت سرعته عند أي لحظة، كذلك يمكن إيجاد سرعة جسم متحرك إذا عُلِم تسارعه عند أي لحظة أي أن:
</div>

$$ s = \int v \, dt = \int \frac{ds}{dt} \, dt $$
$$ v = \int a \, dt = \int \frac{dv}{dt} \, dt $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (5):</strong><br>
يتحرك جسيم في خط مستقيم مبتدئًا من السكون من نقطة ثابتة $O$ بحيث تكون سرعته $v$ بالمتر لكل ثانية مرتبطة بالزمن $t$ بالثواني بالعلاقة $v = 12t - 3t^2$ ، أوجد إزاحة الجسيم عن النقطة الثابتة $O$ بعد مضي زمن قدره $3\text{ sec}$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$ \because s = \int v \, dt = \int (12t - 3t^2) \, dt $$

$$ s = 6t^2 - t^3 + C \quad , \quad s = 0 \text{ عند } t = 0 $$

$$ \therefore 0 = 6(0)^2 - (0)^3 + C $$
$$ C = 0 $$

$$ \therefore s = 6t^2 - t^3 \quad , \quad t = 3\text{ sec} $$

$$ s_{t = 3\text{sec}} = 6(3)^2 - (3)^3 $$
$$ = 27\text{ m} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>115</strong> | الدرس 3-3 تطبيقات على التكامل غير المحدد
</div>
<!-- PAGE_END_115 -->


<!-- PAGE_START_116 -->
### صفحة 116

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 6</b>
<br>
يتحرك جسم من السكون في خط مستقيم مبتدئاً من نقطة ثابتة $O$ ، بحيث كان تسارعه $a$ بالسنتيمتر لكل ثانية مربعة مرتبطة بالزمن $t$ بالثواني بالعلاقة $a = 8 \sin 2t$ ، أوجد سرعة الجسم بعد مضي زمن قدره $\frac{\pi}{2} \text{ sec}$ من لحظة بدء الحركة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
</div>

$$\therefore v = \int a \, dt$$

$$\therefore \int a \, dt = \int 8 \sin 2t \, dt$$

$$v = -8 \frac{\cos 2t}{2} + C \quad , \quad v = 0 \text{ عند } t = 0$$

$$\therefore 0 = -4 \cos 0 + C \Rightarrow C = 4$$

$$\therefore v = -4 \cos 2t + 4 \quad , \quad t = \frac{\pi}{2} \text{ sec}$$

$$v_{t = \frac{\pi}{2} \text{ sec}} = -4 \cos (2) \left(\frac{\pi}{2}\right) + 4$$

$$= -4 \cos \pi + 4$$

$$= 8 \text{ cm/sec}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>مثال 7</b>
<br>
إذا كانت العلاقة بين السرعة $v$ بالمتر لكل ثانية ، والزمن $t$ بالثواني لنقطة مادية متحركة في خط مستقيم بدءاً من نقطة ثابتة $O$ هي $v = 10 + 2t$ ، فأوجد المسافة المقطوعة في $8 \text{ sec}$ من لحظة بدء الحركة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>الحل</b>
</div>

$$\because s = \int v \, dt$$

$$\therefore s = \int (10 + 2t) \, dt$$

$$s = 10t + t^2 + C \quad , \quad s = 0 \text{ عند } t = 0$$

$$0 = 10 (0) + (0)^2 + C \Rightarrow C = 0$$

$$\therefore s = 10t + t^2 \quad , \quad t = 8 \text{ sec}$$

$$s_{t = 8 \text{ sec}} = 10(8) + (8)^2$$

$$= 144 \text{ m}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>116</b> الفصل 3 التكامل غير المحدد
</div>
<!-- PAGE_END_116 -->


<!-- PAGE_START_117 -->
### صفحة 117

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 8</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
يتحرك جسيم في خط مستقيم مبتدئًا من نقطة ثابتة $O$ ، إذا كانت العلاقة بين تسارعه $a$ بالسنتيمتر لكل ثانية مربعة ، والزمن $t$ بالثواني هي $a = 4 \sin \frac{t}{2}$ ، وكانت سرعته الابتدائية $6 \text{ cm/sec}$ ، فأوجد كلاً من سرعة الجسيم، وبعده عن النقطة الثابتة بعد مضي $\pi \text{ sec}$ من لحظة بدء الحركة.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$ \because v = \int a \, dt $$

$$ \therefore v = \int 4 \sin \frac{t}{2} \, dt $$

$$ = -8 \cos \frac{t}{2} + C \quad , \quad v = 6 \text{ cm/sec} \text{ عند } t = 0 $$

$$ 6 = -8 \cos 0 + C $$

$$ 6 = -8 + C \Rightarrow C = 14 $$

$$ \therefore v = -8 \cos \frac{t}{2} + 14 $$

$$ v_{t = \pi \text{ sec}} = -8 \cos \frac{t}{2} + 14 = 14 \text{ cm/sec} $$

$$ \because s = \int v \, dt \quad , \quad v = -8 \cos \frac{t}{2} + 14 $$

$$ \therefore s = \int \left( -8 \cos \frac{t}{2} + 14 \right) dt $$

$$ = -16 \sin \frac{t}{2} + 14t + C \quad , \quad s = 0 \text{ عند } t = 0 $$

$$ \therefore 0 = -16 \sin(0) + 14(0) + C \Rightarrow C = 0 $$

$$ \therefore s = -16 \sin \frac{t}{2} + 14t \quad , \quad t = \pi \text{ sec} $$

$$ \therefore s_{t = \pi \text{ sec}} = -16 \sin \frac{\pi}{2} + 14\pi $$

$$ = (-16 + 14\pi) \text{ cm} $$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 3-3 تطبيقات على التكامل غير المحدد | <strong>117</strong>
</div>
<!-- PAGE_END_117 -->


<!-- PAGE_START_118 -->
### صفحة 118

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين 3-3</h2>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد معادلة منحنى $y = f(x)$ في كل مما يأتي، إذا كان ميل المماس $m$ عند النقطة $(x, y)$ المعطاة والواقعة عليه هو $f'(x)$ :
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
1. $f'(x) = 3x^2 - 2x + 1 \quad , \quad (1, 5)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2. $f'(x) = x^2 (15 - x) \quad , \quad (0, 7)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3. $f'(x) = (4 - x)^3 \quad , \quad (4, -2)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
4. $f'(x) = 3\cos^3 x \sin x \quad , \quad (0, 1)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
5. $f'(x) = \sec^2 x \quad , \quad \left(\frac{\pi}{3}, 0\right)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
6. $f'(x) = (x - 2)(x + 3) \quad , \quad (0, -4)$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
7. إذا كان ميل المماس لمنحنى $y = f(x)$ عند أي نقطة $(x, y)$ واقعة عليه يُعطى بالعلاقة $f'(x) = 3x^2 - 10x + k , k \in \mathbb{R}$ ، فأوجد معادلة هذا المنحنى علمًا بأنه يمر بالنقطتين $(1, 0) ، (0, -3)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
8. دالة مشتقتها الأولى $\frac{dy}{dx} = -2x + 6$ ، وقيمتها العظمى المحلية تساوي $6$. أوجد هذه الدالة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
9. أوجد الدالة التي مشتقتها الأولى $\frac{dy}{dx} = 3x^2 - 3$ ، وقيمتها الصغرى المحلية تساوي $(-4)$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
118 الفصل 3 التكامل غير المحدد
</div>
<!-- PAGE_END_118 -->


<!-- PAGE_START_119 -->
### صفحة 119

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد بُعد جسيم متحرك $s$ بالسنتيمترات عن نقطة ثابتة $O$ عند لحظة زمنية $t$ بالثواني ، إذا كانت سرعته $v$ بالسنتيمتر لكل ثانية في كل مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(10)</b> $v = 2t + 5 , s = 0\text{ cm} , t = 0\text{ sec}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(11)</b> $v = (t - 5)(t + 1) , s = 2\text{ cm} , t = 1\text{ sec}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(12)</b> $v = \cos t + \sin t , s = 1\text{ cm} , t = \frac{\pi}{2}\text{ sec}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(13)</b> $v = \frac{4}{(t - 3)^2} , s = 0\text{ cm} , t = 0\text{ sec}$
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
أوجد كلًّا من سرعة جسيم متحرك في خط مستقيم، وبُعدِه عن نقطة ثابتة $O$ ، عند أيّ لحظة زمنية $t$ بالثواني ، إذا كان تسارعه $a$ بالسنتيمتر لكل ثانية مربعة مُعطى كما في كلٍّ من الحالات الآتية:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(14)</b> $a = 6t + 2 , s = 0\text{ cm} , v = 0\text{ cm/sec} , t = 0\text{ sec}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(15)</b> $a = 8(1 + 2t)^3 , s = 3\text{ cm} , v = 1\text{ cm/sec} , t = 0\text{ sec}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(16)</b> $a = 1 - 4t , s = 5\text{ cm} , v = 0\text{ cm/sec} , t = 0\text{ sec}$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(17)</b> $a = 1 - \cos t , s = 1\text{ cm} , v = 0\text{ cm/sec} , t = 0\text{ sec}$
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>(18)</b> يتحرّك جسيم من نقطة ثابتة $O$ في خط مستقيم. وكان تسارعه $a$ بالسنتيمتر لكل ثانية مربعة عند أي لحظة زمنية $t$ ثانية يُعطى بالعلاقة $a = 3 + 4t$. أوجد سرعة هذا الجسيم عند أي لحظة $t$ ثانية، علمًا بأن سرعته الابتدائية $8\text{ cm/sec}$، ثم أوجد المسافة المقطوعة عند $t = 4\text{ sec}$.
</div>

<br/>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 3-3 تطبيقات على التكامل غير المحدد | <b>119</b>
</div>
<!-- PAGE_END_119 -->


<!-- PAGE_START_120 -->
### صفحة 120

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>اختبار الفصل</h2>
<p><b>أوجد كلًّا من التكاملات الآتية:</b></p>
</div>

$$1) \quad \int x^2 (5x^2 - 8x + 3) \, dx$$

$$2) \quad \int (x^2 - 8x + 16)^{\frac{7}{2}} \, dx$$

$$3) \quad \int 9x \sqrt{x^2 + 12} \, dx$$

$$4) \quad \int \frac{5}{x^2} \left( 1 + \frac{1}{x} \right)^3 \, dx$$

$$5) \quad \int \frac{dx}{x^2 + 6x + 9}$$

$$6) \quad \int \frac{1 - \sin^2 x}{\cos^2 x} \, dx$$

$$7) \quad \int (\tan^4 x - 1) \, dx$$

$$8) \quad \int (\cos^4 x - \sin^4 x) \, dx$$

$$9) \quad \int \frac{\cot x - \csc x}{\sin x} \, dx$$

$$10) \quad \int \frac{\sin x}{\cos^2 x} \, dx$$

$$11) \quad \int (7x - 3)(x + 1) \, dx$$

$$12) \quad \int \frac{(x - 4)^2 - 9}{x - 7} \, dx$$

$$13) \quad \int 12x (x^2 + 1)^5 \, dx$$

$$14) \quad \int \frac{7x}{\sqrt[3]{3x^2 - 5}} \, dx$$

$$15) \quad \int (\cot^3 x + \cot x) \, dx$$

$$16) \quad \int \sec^3 x \cos x \, dx$$

$$17) \quad \int \frac{\sin 2x \cos x}{\sin x} \, dx$$

$$18) \quad \int \frac{2 - \sin^2 x}{\cos^2 x} \, dx$$

$$19) \quad \int \frac{\cos 2x}{\cos x - \sin x} \, dx$$

$$20) \quad \int 7 \sin 3t \, dt$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p><b>21)</b> إذا كانت $f(x) = \cos^2 x \, , \, g(x) = 2x$ فأوجد $\int [f \circ g](x) \, dx$</p>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p><b>22)</b> دالة مشتقتها الأولى $\frac{dy}{dx} = 2x + 1$ وقيمتها الصغرى المحلية تساوي $(-1)$، أوجد هذه الدالة.</p>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p><b>23)</b> إذا كان ميل المماس لمنحنى ما عند أي نقطة $(x, y)$ واقعة عليه هو $\frac{dy}{dx} = \sqrt{x}$، فأوجد معادلة هذا المنحنى، علمًا بأنه يمر بالنقطة $(4, 3)$.</p>
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<p><b>24)</b> إذا كان ميل المماس لمنحنى ما يتعين من العلاقة $\frac{dy}{dx} = 1 - \frac{1}{x^2} \, , \, x \neq 0$، فأوجد معادلة هذا المنحنى، علمًا بأنه يمر بالنقطة $(1, 1)$.</p>
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>الفصل 3:</b> التكامل غير المحدد | <b>اختبار الفصل 3</b> | <b>120</b>
</div>
<!-- PAGE_END_120 -->
