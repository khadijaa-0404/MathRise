

<!-- PAGE_START_124 -->
### صفحة 124

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1>4-1 النظرية الأساسية للتفاضل والتكامل</h1>
<p><em>The Fundamental Theorem of Calculus</em></p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
تعلم أن إيجاد تكامل الدالة $f$ على الفترة المغلقة $[a, b]$ يتطلب تجزيء هذه الفترة، ثم إيجاد قيمة تكامل الدالة كنهاية لمجموع، غير أنه حين تكون الدالة متصلة، فإننا نستطيع إيجاد تكاملها بطريقة تعفينا من تحمل مشاق التجزيئة وإيجاد الغايات. وهذه الطريقة تعتمد على النظرية الأساسية للتفاضل والتكامل، والتي سنقدمها هنا دون برهان لها:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #00a896; padding: 15px; background-color: #f0fdfa; border-radius: 8px;">
<div style="color: #0077b6; font-weight: bold; margin-bottom: 10px;">
دون برهان | نظرية
</div>

إذا كانت $f(x)$ متصلة في الفترة $[a, b]$ ، وكانت $F(x)$ دالة أصلية للدالة $f(x)$ في هذه الفترة ، فإن:

$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$

وعادة ما يُكتب العدد:

$$F(b) - F(a)$$

على الصورة:

$$F(x) \Big|_a^b$$

أي أن:

$$\int_{a}^{b} f(x) \, dx = F(x) \Big|_a^b$$

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong style="background-color: #0077b6; color: white; padding: 3px 8px; border-radius: 3px;">مثال 1</strong>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-top: 10px;">
احسب قيمة $\int_{-1}^{2} (4x^3 + 3x^2 + 2x) \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px; margin-top: 10px;">
<strong style="color: #d90429;">الحل</strong><br>
يتضح أن $F(x) = x^4 + x^3 + x^2$<br>
دالة أصلية لـ $f(x) = 4x^3 + 3x^2 + 2x$<br>
في الفترة $[-1, 2]$
</div>

<br><br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>124</strong> الفصل 4 التكامل المحدد
</div>
<!-- PAGE_END_124 -->


<!-- PAGE_START_125 -->
### صفحة 125

$$\therefore \int_{-1}^{2} (4x^3 + 3x^2 + 2x) \, dx$$

$$= \left[ x^4 + x^3 + x^2 \right]_{-1}^{2}$$

$$= \left[ (2)^4 + (2)^3 + (2)^2 \right] - \left[ (-1)^4 + (-1)^3 + (-1)^2 \right]$$

$$= [16 + 8 + 4] - [1 - 1 + 1]$$

$$= 28 - 1$$

$$= 27$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2)</strong><br>
إذا كانت الدالة $f(x) = x^2 |x|, \, x \in [-2, 2]$ ، فاحسب $\int_{-2}^{2} f(x) \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
يتضح أن $f(x)$ متصلة في الفترة $[-2, 2]$ ، وأن:
</div>

$$f(x) = \begin{cases} -x^3 & , \, -2 \le x \le 0 \\ x^3 & , \, 0 < x \le 2 \end{cases}$$

$$\therefore \int_{-2}^{2} f(x) \, dx = \int_{-2}^{0} f(x) \, dx + \int_{0}^{2} f(x) \, dx$$

$$= \int_{-2}^{0} -x^3 \, dx + \int_{0}^{2} x^3 \, dx$$

$$= \left[ -\frac{x^4}{4} \right]_{-2}^{0} + \left[ \frac{x^4}{4} \right]_{0}^{2}$$

$$= [0 - (-4)] + [4 - 0]$$

$$= 4 + 4$$

$$= 8$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3>إرشادات للدراسة</h3>
<h4>خواص التكامل المحدد</h4>

1. إذا كانت $f(x)$ قابلة للتكامل على $[a, b]$ ، فإن:
</div>

$$\int_{a}^{b} K f(x) \, dx = K \int_{a}^{b} f(x) \, dx$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
حيث $K$ عدد حقيقي.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
2.
</div>

$$\int_{a}^{b} (f \pm g)(x) \, dx = \int_{a}^{b} f(x) \, dx \pm \int_{a}^{b} g(x) \, dx$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
حيث $g(x)$ دالة قابلة للتكامل على $[a, b]$ أيضاً.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
3. إذا وجد عدد حقيقي $c$ ، حيث $c \in [a, b]$ ، وكانت الدالة $f$ قابلة للتكامل على كل من $[a, c] , [c, b]$ ، فإن:
</div>

$$\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
4.
</div>

$$\int_{b}^{a} f(x) \, dx = -\int_{a}^{b} f(x) \, dx$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
5.
</div>

$$\int_{a}^{a} f(x) \, dx = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 4-1 النظرية الأساسية للتفاضل والتكامل | 125
</div>
<!-- PAGE_END_125 -->


<!-- PAGE_START_126 -->
### صفحة 126

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3:</strong> احسب قيمة $\int_{-4}^{0} \frac{2x}{\sqrt{x^2 + 9}} dx$
<br><br>
<strong>الحل:</strong>
</div>

$$ \int_{-4}^{0} \frac{2x}{\sqrt{x^2 + 9}} dx = \int_{-4}^{0} (x^2 + 9)^{-\frac{1}{2}} (2x) dx $$
$$ = \left( 2(x^2 + 9)^{\frac{1}{2}} \right)_{-4}^{0} $$
$$ = \left( 2\sqrt{x^2 + 9} \right)_{-4}^{0} $$
$$ = 2\sqrt{0 + 9} - 2\sqrt{16 + 9} $$
$$ = 6 - 10 $$
$$ = -4 $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 1:</strong> احسب قيمة كل تكامل مما يأتي:
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
a) $\int_{0}^{2} (2x + 1)^5 dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
b) $\int_{0}^{3} \frac{2u + 1}{\sqrt{u^2 + u + 1}} du$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
c) $\int_{-1}^{0} 1 - |x| dx$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4:</strong> احسب قيمة $\int_{0}^{\pi} \sin^3 x dx$
</div>

$$ \therefore \sin^3 x = \sin^2 x \sin x $$
$$ = (1 - \cos^2 x) \sin x $$
$$ = \sin x - \cos^2 x \sin x $$

$$ \therefore \int_{0}^{\pi} \sin^3 x dx = \int_{0}^{\pi} (\sin x - \cos^2 x \sin x) dx $$
$$ = \left( -\cos x + \frac{1}{3} \cos^3 x \right)_{0}^{\pi} $$
$$ = \left( -\cos \pi + \frac{1}{3} \cos^3 \pi \right) - \left( -\cos 0 + \frac{1}{3} \cos^3 0 \right) $$
$$ = \left( 1 - \frac{1}{3} \right) - \left( -1 + \frac{1}{3} \right) $$
$$ = \frac{2}{3} + \frac{2}{3} = \frac{4}{3} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الفصل 4: التكامل المحدد | 126
</div>
<!-- PAGE_END_126 -->


<!-- PAGE_START_127 -->
### صفحة 127

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5:</strong> أثبت أن:
</div>

$$ \int_{\frac{\pi}{4}}^{\frac{5\pi}{4}} \sqrt{\csc^4 x \cot^4 x} \, dx = 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الإثبات:</strong>
</div>

$$ \because \sqrt{\csc^4 x \cot^4 x} = \csc^2 x \cot^2 x $$

$$ \therefore \text{L.H.S} = \int_{\frac{\pi}{4}}^{\frac{5\pi}{4}} (\csc^2 x \cot^2 x) \, dx $$

$$ = \left( -\frac{1}{3} \cot^3 x \right) \Bigg|_{\frac{\pi}{4}}^{\frac{5\pi}{4}} $$

$$ = -\frac{1}{3} \cot^3 \frac{5\pi}{4} + \frac{1}{3} \cot^3 \frac{\pi}{4} $$

$$ = -\frac{1}{3}(1) + \frac{1}{3}(1) $$

$$ = -\frac{1}{3} + \frac{1}{3} $$

$$ = 0 $$

$$ = \text{R.H.S} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 2:</strong> احسب قيمة كل من التكاملات الآتية:
</div>

$$ \text{a)} \quad \int_{0}^{4} \cos \frac{x}{3} \, dx $$

$$ \text{b)} \quad \int_{0}^{\frac{\pi}{3}} \sec x (\sec x + \sec x \tan x) \, dx $$

$$ \text{c)} \quad \int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \frac{1}{\sin^2 x \cos^2 x} \, dx $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 1-4 النظرية الأساسية للتفاضل والتكامل &nbsp;&nbsp;|&nbsp;&nbsp; <strong>127</strong>
</div>
<!-- PAGE_END_127 -->


<!-- PAGE_START_128 -->
### صفحة 128

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 6:</strong> احسب قيمة $\int_{0}^{\frac{\pi}{2}} \cos^5 x \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because \cos^5 x = (\cos^2 x)^2 \cos x$$
$$= (1 - \sin^2 x)^2 \cos x$$
$$= (1 - 2 \sin^2 x + \sin^4 x) \cos x$$
$$= \cos x - 2 \sin^2 x \cos x + \sin^4 x \cos x$$

$$\therefore \int_{0}^{\frac{\pi}{2}} \cos^5 x \, dx = \int_{0}^{\frac{\pi}{2}} (\cos x - 2 \sin^2 x \cos x + \sin^4 x \cos x) \, dx$$
$$= \left( \sin x - \frac{2}{3} \sin^3 x + \frac{1}{5} \sin^5 x \right) \Bigg|_{0}^{\frac{\pi}{2}}$$
$$= \left( \sin \frac{\pi}{2} - \frac{2}{3} \sin^3 \frac{\pi}{2} + \frac{1}{5} \sin^5 \frac{\pi}{2} \right) - \left( \sin 0 - \frac{2}{3} \sin^3 0 + \frac{1}{5} \sin^5 0 \right)$$
$$= \left( 1 - \frac{2}{3} + \frac{1}{5} \right) - 0 = \frac{8}{15}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 7:</strong> احسب قيمة $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin^4 x \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because \sin^4 x = (\sin^2 x)^2$$
$$= \left( \frac{1}{2} (1 - \cos 2x) \right)^2 \qquad \text{\color{red}{لماذا ؟}}$$
$$= \frac{1}{4} (1 - 2 \cos 2x + \cos^2 2x)$$
$$= \frac{1}{4} \left( 1 - 2 \cos 2x + \frac{1}{2} (1 + \cos 4x) \right)$$
$$= \frac{1}{4} \left( \frac{3}{2} - 2 \cos 2x + \frac{1}{2} \cos 4x \right)$$
$$= \frac{1}{8} (3 - 4 \cos 2x + \cos 4x)$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
128 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; <strong>الفصل 4:</strong> التكامل المحدد
</div>
<!-- PAGE_END_128 -->


<!-- PAGE_START_129 -->
### صفحة 129

$$\therefore \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin^4 x \, dx = \frac{1}{8} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} (3 - 4 \cos 2x + \cos 4x) \, dx$$

$$= \frac{1}{8} \left[ 3x - 2 \sin 2x + \frac{1}{4} \sin 4x \right]_{-\frac{\pi}{2}}^{\frac{\pi}{2}}$$

$$= \frac{1}{8} \left[ \left( 3\frac{\pi}{2} - 2 \sin \pi + \frac{1}{4} \sin 2\pi \right) - \left( -\frac{3\pi}{2} - 2 \sin(-\pi) + \frac{1}{4} \sin(-2\pi) \right) \right]$$

$$= \frac{1}{8} \left[ \frac{3\pi}{2} + \frac{3\pi}{2} \right]$$

$$= \frac{3\pi}{8}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (8):</strong> إذا كان $\int_{\frac{\pi}{6}}^{b} \sec^2 x \tan x \, dx = \frac{4}{3}$ ، $b \in \left[0, \frac{\pi}{2}\right]$ ، فأوجد قيمة $b$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because \int_{\frac{\pi}{6}}^{b} \sec^2 x \tan x \, dx = \frac{4}{3}$$

$$\therefore \int_{\frac{\pi}{6}}^{b} \sec x (\sec x \tan x) \, dx = \frac{4}{3}$$

$$\therefore \frac{1}{2} \left[ \sec^2 x \right]_{\frac{\pi}{6}}^{b} = \frac{4}{3}$$

$$\frac{1}{2} \left( \sec^2 b - \sec^2 \frac{\pi}{6} \right) = \frac{4}{3}$$

$$\therefore \sec^2 b - \frac{4}{3} = \frac{8}{3}$$

$$\sec^2 b = 4$$

$$\therefore \cos^2 b = \frac{1}{4}$$

$$\cos b = 1/2 \quad , \quad b \in \left[0, \frac{\pi}{2}\right)$$

$$\therefore b = \frac{\pi}{3}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب (3):</strong> حُلَّ مثال (8) بطريقة أخرى.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 1-4 النظرية الأساسية للتفاضل والتكامل | 129
</div>
<!-- PAGE_END_129 -->


<!-- PAGE_START_130 -->
### صفحة 130

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين (1-4)</h2>

<p>احسب قيمة كل من التكاملات الآتية:</p>
</div>

$$1 \quad \int_{0}^{1} (8x^3 - 9x^2 - 1) \, dx$$

$$2 \quad \int_{-2}^{-1} \left( x^2 + \frac{1}{x^2} \right) dx$$

$$3 \quad \int_{0}^{4} x^2 |x - 2| \, dx$$

$$4 \quad \int_{0}^{2} (|x - 3| + 3) \, dx$$

$$5 \quad \int_{4}^{7} \sqrt{8 - x} \, dx$$

$$6 \quad \int_{1}^{3} x (x^2 - 1)^4 \, dx$$

$$7 \quad \int_{3}^{4} \frac{x}{\sqrt{25 - x^2}} \, dx$$

$$8 \quad \int_{0}^{\frac{\pi}{4}} \tan^3 x \sec^2 x \, dx$$

$$9 \quad \int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{\cos x}{\sin^4 x} \, dx$$

$$10 \quad \int_{0}^{\frac{\pi}{4}} \frac{\sin x}{\cos^5 x} \, dx$$

$$11 \quad \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} \csc^4 x \, dx$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>130</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>الفصل 4: التكامل المحدد</b>
</div>
<!-- PAGE_END_130 -->


<!-- PAGE_START_131 -->
### صفحة 131

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>4-2 تطبيقات هندسية على التكامل المحدد</b><br>
<i>Geometrical Applications of Definite Integration</i>
</div>

<br>

<div dir="rtl" style="text-align: center; font-size: 20px; font-weight: bold;">
مساحة سطح المنطقة المحصورة بين منحنى $f(x)$ والمحور $x$ في الفترة $[a, b]$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
علمنا فيما سبق أنه إذا كانت $f(x)$ متصلة في الفترة $[a, b]$، فإن المساحة $(A)$ الواقعة تحت منحنى الدالة من $a$ إلى $b$ تُعطى بالعلاقة:
</div>

$$A = \int_{a}^{b} f(x) \, dx \quad \text{(عدديًا)} \quad f(x) \ge 0 \text{ إذا كانت}$$

$$A = -\int_{a}^{b} f(x) \, dx = \left| \int_{a}^{b} f(x) \, dx \right| \quad \text{(عدديًا)} \quad f(x) \le 0 \text{ إذا كانت}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 2px solid #a3d9a5; background-color: #f4fbf4; padding: 15px; border-radius: 8px;">
<b>نتيجة:</b><br>
إذا كانت $f(x)$ معرفة في الفترة $[a, b]$ ، حيث $c, d \in [a, b]$ ، $c < d$ ،<br>
والدالة $f(x)$ غير سالبة في الفترتين $[a, c]$ ، $[d, b]$ ، وغير موجبة في الفترة $[c, d]$ ، وقابلة للتكامل على كل فترة من هذه الفترات ، $(A)$ هي مساحة سطح المنطقة المستوية المحصورة بين منحنى $f(x)$ والمحور $x$ في الفترة $[a, b]$ ، فإن:

$$A = \left| \int_{a}^{c} f(x) \, dx \right| + \left| \int_{c}^{d} f(x) \, dx \right| + \left| \int_{d}^{b} f(x) \, dx \right|$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 1px solid #ffcc99; background-color: #fff9f5; padding: 12px; border-radius: 8px;">
<b>البرهان:</b><br>
نفرض أن $A_1$ ، $A_2$ ، $A_3$ هي مساحات أسطح المناطق المستوية المحصورة بين منحنى $f(x)$ ، والمحور $x$ في الفترات $[a, c]$ ، $[c, d]$ ، $[d, b]$ على الترتيب.
</div>

<br>

<div dir="rtl" style="text-align: left; font-size: 14px;">
الدرس 2-4 تطبيقات هندسية على التكامل المحدد | <b>131</b>
</div>
<!-- PAGE_END_131 -->


<!-- PAGE_START_132 -->
### صفحة 132

$$\therefore A_1 = \int_a^c f(x) \, dx = \left| \int_a^c f(x) \, dx \right|$$

$$A_2 = -\int_c^d f(x) \, dx = \left| \int_c^d f(x) \, dx \right|$$

$$A_3 = \int_d^b f(x) \, dx = \left| \int_d^b f(x) \, dx \right|$$

$$\because A = A_1 + A_2 + A_3$$

$$\therefore A = \left| \int_a^c f(x) \, dx \right| + \left| \int_c^d f(x) \, dx \right| + \left| \int_d^b f(x) \, dx \right|$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1:</strong> أوجد مساحة سطح المنطقة المحصورة بين المحور $x$ ومنحنى $f(x) = x^2 - 4x$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
نوجد نقاط تقاطع منحنى الدالة مع المحور $x$.
</div>

$$x^2 - 4x = 0 \Rightarrow x(x - 4) = 0$$

$$\Rightarrow x = 0 \text{ أو } x = 4$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقطتا التقاطع هما $(0, 0) \, , \, (4, 0)$. ويتضح أن $f(x)$ متصلة في الفترة $[0, 4]$؛ لذا فهي قابلة للتكامل على هذه الفترة.
</div>

$$\because f(x) \le 0 \quad \forall x \in [0, 4]$$

$$\therefore A = \left| \int_0^4 f(x) \, dx \right|$$

$$= \left| \int_0^4 (x^2 - 4x) \, dx \right|$$

$$= \left| \left( \frac{x^3}{3} - 2x^2 \right)_0^4 \right|$$

$$= \left| \left( \frac{64}{3} - 32 \right) - (0) \right|$$

$$= \frac{32}{3} \text{ وحدة مربعة}$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>الفصل 4:</strong> التكامل المحدد &nbsp;&nbsp;|&nbsp;&nbsp; <strong>132</strong>
</div>
<!-- PAGE_END_132 -->


<!-- PAGE_START_133 -->
### صفحة 133

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (2)</strong>
<br>
إذا كانت $f(x) = \sin x$ ، فأوجد مساحة سطح المنطقة المحصورة بين منحنى $f(x)$ والمحور $x$ في الفترة $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ .
<br><br>
<strong>الحل</strong>
<br>
نوجد نقاط تقاطع منحنى $f(x)$ مع المحور $x$ في الفترة $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ .
</div>

$$\sin x = 0 \Rightarrow x = 0$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
إذن نقطة التقاطع هي $(0, 0)$ . ويتضح أن الدالة متصلة في الفترة $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ ؛ لذا فهي قابلة للتكامل على الفترتين $\left[-\frac{\pi}{2}, 0\right]$ ، $\left[0, \frac{\pi}{2}\right]$ .
</div>

$$\because f(x) \le 0 \quad \forall x \in \left[-\frac{\pi}{2}, 0\right]$$

$$f(x) \ge 0 \quad \forall x \in \left[0, \frac{\pi}{2}\right]$$

$$\therefore A = \left| \int_{-\frac{\pi}{2}}^{0} f(x) \, dx \right| + \left| \int_{0}^{\frac{\pi}{2}} f(x) \, dx \right|$$

$$= \left| \int_{-\frac{\pi}{2}}^{0} \sin x \, dx \right| + \left| \int_{0}^{\frac{\pi}{2}} \sin x \, dx \right|$$

$$= \left| \left[-\cos x\right]_{-\frac{\pi}{2}}^{0} \right| + \left| \left[-\cos x\right]_{0}^{\frac{\pi}{2}} \right|$$

$$= \left| -\cos 0 + \cos\left(-\frac{\pi}{2}\right) \right| + \left| -\cos \frac{\pi}{2} + \cos 0 \right|$$

$$= |-1 + 0| + |0 + 1|$$

$$= 1 + 1$$

$$= 2 \text{ وحدة مربعة}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (3)</strong>
<br>
أوجد مساحة سطح المنطقة المحصورة بين المحور $x$، ومنحنى $f(x) = 4x^3 - 12x^2 + 8x$ .
<br><br>
<strong>الحل</strong>
<br>
نوجد نقاط تقاطع منحنى $f(x)$ مع المحور $x$ .
</div>

$$4x^3 - 12x^2 + 8x = 0$$

$$\Rightarrow 4x(x^2 - 3x + 2) = 0$$

$$\Rightarrow 4x(x - 1)(x - 2) = 0$$

$$\Rightarrow x = 2 \quad \text{أو} \quad x = 1 \quad \text{أو} \quad x = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>133</strong> الدرس 4-2 تطبيقات هندسية على التكامل المحدد
</div>
<!-- PAGE_END_133 -->


<!-- PAGE_START_134 -->
### صفحة 134

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقاط التقاطع هي $(0, 0) , (1, 0) , (2, 0)$<br>
بما أن الدالة متصلة في الفترة $[0, 2]$؛ إذن الدالة $f(x)$ قابلة للتكامل على الفترتين $[0, 1] , [1, 2]$
</div>

$$\because f(x) \le 0 \quad \forall x \in [1, 2]$$

$$\therefore A = \left| \int_{0}^{1} f(x) \, dx \right| + \left| \int_{1}^{2} f(x) \, dx \right|$$

$$= \left| \int_{0}^{1} (4x^3 - 12x^2 + 8x) \, dx \right| + \left| \int_{1}^{2} (4x^3 - 12x^2 + 8x) \, dx \right|$$

$$= \left| \left[ x^4 - 4x^3 + 4x^2 \right]_{0}^{1} \right| + \left| \left[ x^4 - 4x^3 + 4x^2 \right]_{1}^{2} \right|$$

$$= \left| (1 - 4 + 4) - (0) \right| + \left| (16 - 32 + 16) - (1 - 4 + 4) \right|$$

$$= |1| + |-1|$$

$$= 2 \text{ وحدة مربعة}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>تدريب 1:</strong><br>
أوجد مساحة سطح المنطقة المحصورة بين المحور $x$، ومنحنى كل دالة مما يأتي:
</div>

$$\text{a) } f(x) = x^3 - 4x$$

$$\text{b) } f(x) = \sin 2x \quad , \quad \forall x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4:</strong><br>
إذا كانت $f(x) = k x^2 + 1 , k > 0$، وكانت المساحة المحصورة بين منحنى $f(x)$، والمحور $x$ في الفترة $[-3, 1]$ تساوي $32$ وحدة مربعة، فأوجد قيمة $k$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because f(x) = k x^2 + 1 \quad , \quad k > 0$$

$$\therefore A = \int_{a}^{b} f(x) \, dx$$

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
الفصل 4: التكامل المحدد | 134
</div>
<!-- PAGE_END_134 -->


<!-- PAGE_START_135 -->
### صفحة 135

$$\Rightarrow 32 = \int_{-3}^{1} (kx^2 + 1) \, dx$$

$$32 = \left[ \frac{kx^3}{3} + x \right]_{-3}^{1}$$

$$32 = \left[ \left( \frac{k}{3} (1)^3 + 1 \right) - \left( \frac{k}{3} (-3)^3 + (-3) \right) \right]$$

$$32 = \left[ \frac{k}{3} + 1 + \frac{27k}{3} + 3 \right]$$

$$32 = \frac{28k}{3} + 4$$

$$\Rightarrow \frac{28k}{3} = 28$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$$\therefore k = 3$$
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b style="font-size: 18px; color: #1a5276;">مثال 5</b>

باستعمال التكامل أوجد مساحة سطح المنطقة المحصورة بين القطعة المستقيمة $CD$، والمحور $x$، حيث $C(-2, 1)$ ، $D(1, 10)$.

<b style="font-size: 18px; color: #1a5276;">الحل</b>

ميل المستقيم الذي يمر بالنقطتين $C(-2, 1)$ ، $D(1, 10)$ هو:

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$
$$= \frac{10 - 1}{1 + 2}$$
$$= 3$$

$\therefore$ معادلة المستقيم $CD$ هي:

$$y - y_1 = m(x - x_1)$$
$$y - 10 = 3(x - 1)$$
$$y - 10 = 3x - 3$$
$$y = 3x + 7$$

$$\because y > 0 \quad \forall x \in [-2, 1]$$

$$\therefore A = \int_{-2}^{1} y \, dx$$

$$= \int_{-2}^{1} (3x + 7) \, dx$$

$$= \left[ \frac{3x^2}{2} + 7x \right]_{-2}^{1}$$

$$= \left[ \left( \frac{3}{2} + 7 \right) - \left( \frac{12}{2} - 14 \right) \right]$$

$$= \frac{33}{2} \text{ وحدة مربعة}$$

</div>

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>135</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>الدرس 4-2 تطبيقات هندسية على التكامل المحدد</b>
</div>
<!-- PAGE_END_135 -->


<!-- PAGE_START_136 -->
### صفحة 136

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>مساحة سطح المنطقة المحصورة بين منحنيي $f_1(x)$ ، $f_2(x)$ في الفترة $[a, b]$</h2>

إذا كانت كل من $f_1(x)$ ، $f_2(x)$ متصلة في الفترة $[a, b]$ وكانت $f_1(x) \neq f_2(x) \quad \forall x \in (a, b)$

كما في كل شكل أدناه، فإن مساحة سطح المنطقة $A$ المحصورة بين منحنيي $f_1(x)$ ، $f_2(x)$ تساوي القيمة المطلقة لتكامل $(f_1 - f_2)(x)$ على الفترة $[a, b]$ ، أي أن:
</div>

$$A = \left| \int_a^b (f_1 - f_2)(x) \, dx \right|$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 6:</strong> أوجد مساحة سطح المنطقة المحصورة بين منحنى الدالة $y = 8x - 3x^2$ ، والمستقيم $y = 2x$

<br>

<strong>الحل:</strong>

نوجد نقاط تقاطع المنحنى والمستقيم بحل معادلتيهما كالآتي:
</div>

$$\because 8x - 3x^2 = 2x$$
$$\Rightarrow 3x^2 - 6x = 0$$
$$\Rightarrow 3x(x - 2) = 0$$
$$\Rightarrow x = 0 \quad \text{أو} \quad x = 2$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقطتا التقاطع هما $(0, 0) , (2, 4)$
<br>
$\because 8x - 3x^2 \geq 2x \quad \forall x \in [0, 2]$
</div>

$$\therefore A = \left| \int_0^2 \left[ (8x - 3x^2) - (2x) \right] dx \right|$$
$$= \left| \int_0^2 (6x - 3x^2) \, dx \right|$$
$$= \left| \left[ 3x^2 - x^3 \right]_0^2 \right|$$
$$= \left| [(12 - 8) - (0)] \right|$$
$$= 4 \quad \text{وحدة مربعة}$$

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الفصل 4</strong> التكامل المحدد | <strong>136</strong>
</div>
<!-- PAGE_END_136 -->


<!-- PAGE_START_137 -->
### صفحة 137

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (7)</strong><br>
أوجد مساحة سطح المنطقة المحصورة بين منحنيي الدالتين $y = \sqrt{x} \text{ , } y = x^2$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
نوجد نقاط تقاطع المنحنيين كالأتي:
</div>

$$\because x^2 = \sqrt{x}$$
$$\Rightarrow x^4 = x$$
$$\Rightarrow x^4 - x = 0$$
$$\Rightarrow x(x^3 - 1) = 0$$
$$\Rightarrow x(x - 1)(x^2 + x + 1) = 0$$
$$\Rightarrow x = 0 \quad \text{أو} \quad x = 1$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقطتا التقاطع هما $(1, 0) , (0, 0)$
</div>

$$\because \sqrt{x} \ge x^2 \quad \forall x \in [0, 1]$$

$$\therefore A = \left| \int_{0}^{1} (\sqrt{x} - x^2) \, dx \right|$$
$$= \left| \left[ \frac{2}{3} x^{\frac{3}{2}} - \frac{1}{3} x^3 \right]_{0}^{1} \right|$$
$$= \left| \left( \frac{2}{3} - \frac{1}{3} \right) - (0) \right|$$
$$= \frac{1}{3} \quad \text{وحدة مربعة}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال (8)</strong><br>
أوجد مساحة سطح المنطقة المحصورة بين منحنيي الدالتين $y = \sin x \text{ , } y = \cos x$، والمحور $y$ في الفترة $\left[0, \frac{\pi}{4}\right]$ مقرباً الناتج إلى منزلة عشرية واحدة.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because \cos x \ge \sin x \quad \forall x \in \left[0, \frac{\pi}{4}\right]$$

$$\therefore A = \left| \int_{0}^{\frac{\pi}{4}} (\cos x - \sin x) \, dx \right|$$
$$= \left| \left[ \sin x + \cos x \right]_{0}^{\frac{\pi}{4}} \right|$$
$$= \left| \left( \sin \frac{\pi}{4} + \cos \frac{\pi}{4} \right) - (\sin 0 + \cos 0) \right|$$
$$= \left| \left( \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} \right) - (0 + 1) \right|$$
$$= |\sqrt{2} - 1|$$
$$\approx 0.4 \quad \text{وحدة مربعة}$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>137</strong> | الدرس 4-2 تطبيقات هندسية على التكامل المحدد
</div>
<!-- PAGE_END_137 -->


<!-- PAGE_START_138 -->
### صفحة 138

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 9:</strong> أوجد مساحة سطح المنطقة المحصورة بين منحنيي الدالتين $y = x^2 - 2x \quad , \quad y = 6x - x^2$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
نوجد نقاط تقاطع المنحنيين كالآتي:
</div>

$$\because 6x - x^2 = x^2 - 2x$$
$$\Rightarrow 2x^2 - 8x = 0$$
$$\Rightarrow 2x(x - 4) = 0$$
$$\Rightarrow x = 0 \quad \text{أو} \quad x = 4$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقطتا التقاطع هما $(0, 0) , (4, 8)$<br>
$\because 6x - x^2 \ge x^2 - 2x \quad \forall x \in [0, 4]$
</div>

$$\therefore A = \left| \int_{0}^{4} [(6x - x^2) - (x^2 - 2x)] \, dx \right|$$
$$= \left| \int_{0}^{4} [8x - 2x^2] \, dx \right|$$
$$= \left| \left( 4x^2 - \frac{2}{3}x^3 \right)_{0}^{4} \right|$$
$$= \left| \left( 64 - \frac{128}{3} \right) - (0) \right|$$
$$= \left| \frac{64}{3} \right|$$
$$= \frac{64}{3} \quad \text{وحدة مربعة}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 10:</strong> أوجد مساحة سطح المنطقة المحصورة بين منحنى الدالة $y = 2 - x^2$ ، والمستقيم $y = -x$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong><br>
نوجد نقاط تقاطع المنحنى والمستقيم بحل معادلتهما كالآتي:
</div>

$$\because 2 - x^2 = -x$$
$$\Rightarrow x^2 - x - 2 = 0$$
$$\Rightarrow (x + 1)(x - 2) = 0$$
$$\Rightarrow x = -1 \quad \text{أو} \quad x = 2$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>138</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>الفصل 4: التكامل المحدد</strong>
</div>
<!-- PAGE_END_138 -->


<!-- PAGE_START_139 -->
### صفحة 139

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ نقطتا التقاطع هما $(2, -2)$ ، $(-1, 1)$.
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because 2 - x^2 \ge -x \quad \forall x \in [-1, 2]$
</div>

$$ \therefore A = \left| \int_{-1}^{2} [(2 - x^2) - (-x)] \, dx \right| $$

$$ = \left| \int_{-1}^{2} (2 + x - x^2) \, dx \right| $$

$$ = \left| \left[ 2x + \frac{1}{2} x^2 - \frac{1}{3} x^3 \right]_{-1}^{2} \right| $$

$$ = \left| \left( 4 + 2 - \frac{8}{3} \right) - \left( -2 + \frac{1}{2} + \frac{1}{3} \right) \right| $$

$$ = \left| \frac{10}{3} + \frac{7}{6} \right| $$

$$ = \left| \frac{9}{2} \right| $$

$$ = 4.5 \text{ وحدة مربعة} $$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
### <strong>تدريب 2</strong>

أوجد مساحة سطح المنطقة المحصورة بين المحور $x$، ومنحنى الدالة $y = x^3 + 5x$، والمستقيم $x = 4$.
</div>

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 2-4 تطبيقات هندسية على التكامل المحدد | 139
</div>
<!-- PAGE_END_139 -->


<!-- PAGE_START_140 -->
### صفحة 140

<div dir="rtl" style="text-align: center; font-size: 22px; font-weight: bold; margin-bottom: 20px;">
تمارين (2 - 4)
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>1</b> أوجد مساحة سطح المنطقة المحصورة بين المحور $x$ ومنحني الدالة $y = 2x - x^2$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>2</b> أوجد مساحة سطح المنطقة المحصورة بين المحور $x$ والمستقيمين $x = 1$ ، $x = 3$ ومنحني الدالة $y = x^2 + 1$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>3</b> أوجد مساحة سطح المنطقة المحصورة بين منحني الدالة $y = \cos x$ والمحور $x$ في الفترة $[0, \pi]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>4</b> أوجد مساحة سطح المنطقة المحصورة بين المحور $x$ ومنحني الدالة $y = \csc^2 x \quad \forall x \in \left[\frac{\pi}{6}, \frac{\pi}{3}\right]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>5</b> أوجد مساحة سطح المنطقة المحصورة بين منحني الدالة $y = 3x^2$ والمستقيم $y = 6x$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>6</b> أوجد مساحة سطح المنطقة المحصورة بين منحنيي الدالتين $y = x^2$ ، $y = 4 - x^2$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>7</b> أوجد مساحة سطح المنطقة المحصورة بين منحنيي الدالتين $y = \sin x$ ، $y = \cos x \quad \forall x \in \left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>8</b> أوجد مساحة سطح المنطقة المحصورة بين منحني الدالة $y = x^2 - 2x$ ، والمستقيم $y = -3$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>9</b> أوجد مساحة سطح المنطقة المحصورة بين منحني الدالة $y = \sqrt[3]{x}$ ، والمستقيم $y = x$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>10</b> إذا كانت مساحة سطح المنطقة المحصورة بين منحني الدالة $y = 3x^2 + 4x + k$ ، والمحور $x$، والمستقيمين $x = 2$ ، $x = 3$ ، تساوي $25$ وحدة مربعة، فأوجد قيمة $k$.
</div>

<br><hr>

<div dir="rtl" style="text-align: justify; font-size: 14px;">
<b>الفصل 4:</b> التكامل المحدد 
<span style="float: left;"><b>140</b></span>
</div>
<!-- PAGE_END_140 -->


<!-- PAGE_START_141 -->
### صفحة 141

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h1><b>4-3 التكامل بالتعويض</b></h1>
<p><b><i>Integration by Substitution</i></b></p>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
إن إيجاد تكامل دالة متصلة بالنظرية الأساسية للتفاضل والتكامل يتطلب وجود دالة أصلية لهذه الدالة، ونظراً لأننا لا نعرف إلا الدوال الأصلية لعدد قليل من الدوال، برز لدينا التساؤل عن كيفية إيجاد تكامل دالة متصلة لا تكون من بين هذه الدوال، والتي تحتوي على إحدى التعابير الرياضية الآتية:
</div>

$$ \sqrt{a^2 - x^2}, \, \sqrt{a^2 + x^2}, \, \sqrt{x^2 - a^2}, \, a^2 - x^2, \, a^2 + x^2 \text{ أو } x^2 - a^2, \, a > 0 $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
في مثل هذه الحالات نحاول إيجاد طريقة ما نحول بها الدالة التي لدينا إلى دالة أخرى تكون على صورة من الصور القياسية التي نعرفها، وبهذا نتمكن من إيجاد تكاملها، ومن بين هذه الطرائق طريقة هامة تسمى <b>التكامل بالتعويض</b>، وتعتمد على النظرية الآتية التي سنقدمها بدون برهان.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px; border: 2px solid #008080; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
<h3 style="color: #008080; margin-top: 0;"><b>نظرية التعويض</b></h3>

إذا كانت $f(x)$ متصلة في الفترة $[a, b]$، ووجدت $g(x)$ متصلة، وقابلة للاشتقاق، والدالة المشتقة لها متصلة في الفترة $[c, d]$، وكانت:

$$ g(c) = a, \, g(d) = b \quad \forall \theta \in (c, d) $$

تكون:

$$ g(\theta) \in (a, b) $$

فإن:

$$ \int_{a}^{b} f(x) \, dx = \int_{c}^{d} f(g(\theta)) \, g'(\theta) \, d\theta $$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
سنستعمل الجدول أدناه للتعويض عن الدوال السابقة بدوال مثلثية.
</div>

<br>

| التعويضات المثلثية | التعابير الرياضية |
| :---: | :---: |
| $x = \sqrt{\frac{a}{b}} \tan \theta$ | $\sqrt{a + bx^2} \text{ أو } a + bx^2$ |
| $x = \sqrt{\frac{a}{b}} \sin \theta$ | $\sqrt{a - bx^2} \text{ أو } a - bx^2$ |
| $x = \sqrt{\frac{a}{b}} \sec \theta$ | $\sqrt{bx^2 - a} \text{ أو } bx^2 - a$ |

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 3-4 التكامل بالتعويض &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>141</b>
</div>
<!-- PAGE_END_141 -->


<!-- PAGE_START_142 -->
### صفحة 142

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>ملاحظة:</strong><br>
من الجدول السابق لتطبيق نظرية التعويض يجب أن تكون التعابير الرياضية الآتية:
$$a + bx^2 , a - bx^2 , bx^2 - a , a > 0 , b > 0$$
في مقام الدالة المراد إيجاد تكاملها. أما التعابير الرياضية الآتية:
$$\sqrt{a + bx^2} , \sqrt{a - bx^2} , \sqrt{bx^2 - a} , a > 0 , b > 0$$
من الممكن أن تكون في بسط الدالة أو مقامها.<br>
وسنوضح كيفية تطبيق نظرية التعويض من خلال الأمثلة الآتية:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 1</strong><br>
احسب قيمة $\int_{0}^{1} \sqrt{1 - x^2} \, dx$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong><br>
يتضح أن $f(x) = \sqrt{1 - x^2}$<br>
متصلة في الفترة $[0, 1]$؛ لذا فهي قابلة للتكامل على هذه الفترة، غير أن هذه الدالة ليست من الدوال القياسية التي نعرف لها دوال أصلية إلا أنه يمكن تحويلها إلى دالة قياسها كالآتي:
</div>

$$\because f(x) = \sqrt{1 - x^2}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\therefore$ دالة التعويض هي:
</div>

$$x = g(\theta) = \sqrt{\frac{a}{b}} \sin\theta \quad \forall x \in [0, 1]$$

$$= \sin\theta, \quad a = 1, \quad b = 1$$

$$\Rightarrow g'(\theta) = \cos\theta$$

$$\therefore f(x) = \sqrt{1 - x^2} = \sqrt{1 - \sin^2\theta}$$

$$= \sqrt{\cos^2\theta} \qquad \text{\textcolor{red}{لماذا ؟}}$$

$$= \cos\theta$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ولإيجاد حدود التكامل لـ $g(\theta)$ نتبع ما يأتي:
</div>

$$x = 0 \Rightarrow g(\theta) = 0 \Rightarrow \sin\theta = 0 \Rightarrow \theta = 0$$

$$x = 1 \Rightarrow g(\theta) = 1 \Rightarrow \sin\theta = 1 \Rightarrow \theta = \frac{\pi}{2}$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
142 &nbsp;&nbsp;&nbsp;&nbsp; <strong>الفصل 4</strong> التكامل المحدد
</div>
<!-- PAGE_END_142 -->


<!-- PAGE_START_143 -->
### صفحة 143

<div dir="rtl" style="text-align: right; font-size: 16px;">
من الواضح أنه: $\forall \theta \in [0, \frac{\pi}{2}]$<br>
تكون: $x \in [0, 1]$<br>
نلاحظ أن $g(\theta)$ يتوفر فيها الشروط الآتية:
<ul>
  <li>متصلة في الفترة $[0, \frac{\pi}{2}]$</li>
  <li>قابلة للاشتقاق في الفترة $(0, \frac{\pi}{2})$</li>
  <li>الدالة المشتقة $g'(\theta)$ متصلة في الفترة $[0, \frac{\pi}{2}]$</li>
</ul>
ومن الواضح أنه $\forall \theta \in [0, \frac{\pi}{2}]$ تكون $x \in [0, 1]$<br><br>
$\therefore f(x)$ ، $g(\theta)$ يتوفر فيهما شروط نظرية التعويض
</div>

$$\int_{0}^{1} f(x) \, dx = \int_{0}^{\frac{\pi}{2}} f(g(\theta)) \, g'(\theta) \, d\theta$$

$$\Rightarrow \int_{0}^{1} \sqrt{1 - x^2} \, dx = \int_{0}^{\frac{\pi}{2}} \sqrt{1 - \sin^2 \theta} \, (\cos \theta) \, d\theta$$

$$= \int_{0}^{\frac{\pi}{2}} \sqrt{\cos^2 \theta} \, (\cos \theta) \, d\theta$$

$$= \int_{0}^{\frac{\pi}{2}} \cos^2 \theta \, d\theta$$

$$= \int_{0}^{\frac{\pi}{2}} \frac{1}{2} (1 + \cos 2\theta) \, d\theta \qquad \text{\textcolor{red}{لماذا ؟}}$$

$$= \frac{1}{2} \left( \theta + \frac{1}{2} \sin 2\theta \right) \Big|_{0}^{\frac{\pi}{2}}$$

$$= \left[ \frac{1}{2} \left( \frac{\pi}{2} + \frac{1}{2} \sin \pi \right) - \frac{1}{2} \left( 0 + \frac{1}{2} \sin 0 \right) \right]$$

$$= \left[ \frac{1}{2} \left( \frac{\pi}{2} + 0 \right) - \frac{1}{2} (0 + 0) \right]$$

$$= \left[ \frac{\pi}{4} - 0 \right]$$

$$= \frac{\pi}{4}$$

<br>

---
<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>143</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>الدرس 3-4 التكامل بالتعويض</b>
</div>
<!-- PAGE_END_143 -->


<!-- PAGE_START_144 -->
### صفحة 144

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 2</strong>
<br>
احسب قيمة $\int_{0}^{\frac{3}{4}} \frac{12}{\sqrt{9 - 4x^2}} \, dx$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
<br><br>
$\because f(x) = \frac{12}{\sqrt{9 - 4x^2}}$
<br><br>
$\therefore$ دالة التعويض هي:
</div>

$$x = g(\theta) = \sqrt{\frac{a}{b}} \sin\theta , \quad \forall x \in \left[0, \frac{3}{4}\right]$$

$$= \sqrt{\frac{9}{4}} \sin\theta , \quad a = 9 , \ b = 4$$

$$= \frac{3}{2} \sin\theta$$

$$\Rightarrow g'(\theta) = \frac{3}{2} \cos\theta$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ولإيجاد حدود التكامل لـ $g(\theta)$ نتبع ما يأتي:
</div>

$$x = 0 \Rightarrow \frac{3}{2} \sin\theta = 0 \Rightarrow \sin\theta = 0 \Rightarrow \theta = 0 ,$$

$$x = \frac{3}{4} \Rightarrow \frac{3}{2} \sin\theta = \frac{3}{4} \Rightarrow \sin\theta = \frac{1}{2} \Rightarrow \theta = \frac{\pi}{6}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن الواضح أنه $\forall \theta \in \left[0, \frac{\pi}{6}\right]$ تكون $x \in \left[0, \frac{3}{4}\right]$
<br>
$\because$ شروط نظرية التعويض متوفرة
</div>

$$\therefore \int_{0}^{\frac{3}{4}} f(x) \, dx = \int_{0}^{\frac{\pi}{6}} f(g(\theta)) \, g'(\theta) \, d\theta$$

$$\Rightarrow \int_{0}^{\frac{3}{4}} \frac{12}{\sqrt{9 - 4x^2}} \, dx = \int_{0}^{\frac{\pi}{6}} \frac{12}{\sqrt{9 - 9\sin^2\theta}} \left( \frac{3}{2} \cos\theta \right) d\theta$$

$$= \int_{0}^{\frac{\pi}{6}} \frac{12}{3 \cos\theta} \left( \frac{3}{2} \cos\theta \right) d\theta$$

$$= \int_{0}^{\frac{\pi}{6}} 6 \, d\theta$$

$$= 6 (\theta) \Big|_{0}^{\frac{\pi}{6}}$$

$$= 6 \left[ \frac{\pi}{6} - 0 \right]$$

$$= \pi$$

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الفصل 4</strong> التكامل المحدد &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>144</strong>
</div>
<!-- PAGE_END_144 -->


<!-- PAGE_START_145 -->
### صفحة 145

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 3:</strong> احسب قيمة $\int_{\sqrt{3}}^{3\sqrt{3}} \frac{3}{x^2 + 9} \, dx$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>

$$\because f(x) = \frac{3}{x^2 + 9}$$

$\therefore$ دالة التعويض هي:
$$x = g(\theta) = \sqrt{\frac{a}{b}} \tan\theta$$
$$= \sqrt{\frac{9}{1}} \tan\theta$$
$$= 3 \tan\theta$$
$$g'(\theta) = 3 \sec^2\theta$$

ولإيجاد حدود التكامل لـ $g(\theta)$ نتبع ما يأتي:
$$x = \sqrt{3} \Rightarrow 3 \tan\theta = \sqrt{3} \Rightarrow \tan\theta = \frac{\sqrt{3}}{3} \Rightarrow \theta = \frac{\pi}{6} ,$$
$$x = 3\sqrt{3} \Rightarrow 3 \tan\theta = 3\sqrt{3} \Rightarrow \tan\theta = \sqrt{3} \Rightarrow \theta = \frac{\pi}{3} ,$$

ومن الواضح أنه $\forall \theta \in \left[ \frac{\pi}{6}, \frac{\pi}{3} \right]$ تكون $x \in \left[ \sqrt{3}, 3\sqrt{3} \right]$

$\because$ شروط نظرية التعويض متوفرة
$$\therefore \int_{\sqrt{3}}^{3\sqrt{3}} f(x) \, dx = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} f(g(\theta)) g'(\theta) \, d\theta$$

$$\Rightarrow \int_{\sqrt{3}}^{3\sqrt{3}} \frac{3}{x^2 + 9} \, dx = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{3}{9 \tan^2\theta + 9} (3 \sec^2\theta) \, d\theta$$

$$= \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{9 \sec^2\theta}{9 (\tan^2\theta + 1)} \, d\theta$$

$$= \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sec^2\theta}{\sec^2\theta} \, d\theta$$

$$= \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} d\theta$$

$$= (\theta) \Big|_{\frac{\pi}{6}}^{\frac{\pi}{3}}$$

$$= \left[ \frac{\pi}{3} - \frac{\pi}{6} \right] = \frac{\pi}{6}$$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
الدرس 3-4 التكامل بالتعويض | 145
</div>
<!-- PAGE_END_145 -->


<!-- PAGE_START_146 -->
### صفحة 146

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 4</strong>
<br>
احسب قيمة $\int_{\frac{\sqrt{3}}{2}}^{\frac{3\sqrt{3}}{2}} \frac{8x^2}{4x^2 + 9} \, dx$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="color: blue;">الحل</h3>

$$\because f(x) = \frac{8x^2}{4x^2 + 9}$$

$$\therefore \text{دالة التعويض هي:}$$

$$x = g(\theta) = \sqrt{\frac{a}{b}} \tan\theta$$
$$= \sqrt{\frac{9}{4}} \tan\theta$$
$$= \frac{3}{2} \tan\theta$$
$$g'(\theta) = \frac{3}{2} \sec^2\theta$$

ولإيجاد حدود التكامل لـ $g(\theta)$ نتبع ما يأتي:

$$\therefore x = \frac{\sqrt{3}}{2} \Rightarrow \frac{3}{2} \tan\theta = \frac{\sqrt{3}}{2} \Rightarrow \tan\theta = \frac{1}{\sqrt{3}} \Rightarrow \theta = \frac{\pi}{6}$$

$$x = \frac{3\sqrt{3}}{2} \Rightarrow \frac{3}{2} \tan\theta = \frac{3\sqrt{3}}{2} \Rightarrow \tan\theta = \sqrt{3} \Rightarrow \theta = \frac{\pi}{3}$$

ومن الواضح أنه $\forall \theta \in \left[ \frac{\pi}{6}, \frac{\pi}{3} \right]$ تكون $x \in \left[ \frac{\sqrt{3}}{2}, \frac{3\sqrt{3}}{2} \right]$

$$\because \text{شروط نظرية التعويض متوفرة}$$

$$\therefore \int_{\frac{\sqrt{3}}{2}}^{\frac{3\sqrt{3}}{2}} f(x) \, dx = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} f(g(\theta)) \, g'(\theta) \, d\theta$$

$$\Rightarrow \int_{\frac{\sqrt{3}}{2}}^{\frac{3\sqrt{3}}{2}} \frac{8x^2}{4x^2 + 9} \, dx = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \left( \frac{18 \tan^2\theta}{9 \tan^2\theta + 9} \right) \left( \frac{3}{2} \sec^2\theta \right) d\theta$$

$$= \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \left( \frac{18 \tan^2\theta}{9 \sec^2\theta} \right) \left( \frac{3}{2} \sec^2\theta \right) d\theta$$

</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px; border-top: 1px solid #ccc; padding-top: 5px;">
<strong>146</strong> | الفصل 4: التكامل المحدد
</div>
<!-- PAGE_END_146 -->


<!-- PAGE_START_147 -->
### صفحة 147

$$= 3 \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \tan^2 \theta \, d\theta$$

$$= 3 \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} (\sec^2 \theta - 1) \, d\theta$$

$$= 3 \left[ \tan \theta - \theta \right]_{\frac{\pi}{6}}^{\frac{\pi}{3}}$$

$$= 3 \left[ \left( \tan \frac{\pi}{3} - \frac{\pi}{3} \right) - \left( \tan \frac{\pi}{6} - \frac{\pi}{6} \right) \right]$$

$$= 3 \left[ \left( \sqrt{3} - \frac{\pi}{3} \right) - \left( \frac{1}{\sqrt{3}} - \frac{\pi}{6} \right) \right]$$

$$= 3 \left[ \sqrt{3} - \frac{\pi}{3} - \frac{1}{\sqrt{3}} + \frac{\pi}{6} \right]$$

$$= 3 \left[ \frac{2\sqrt{3}}{3} - \frac{\pi}{6} \right]$$

$$= 2\sqrt{3} - \frac{\pi}{2}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 5:</strong> احسب قيمة $\int_{2}^{7} \frac{5}{x^2 - 4x + 29} \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل</strong>
</div>

$$\because f(x) = \frac{5}{x^2 - 4x + 29}$$

$$= \frac{5}{(x - 2)^2 + 25} \qquad \text{لماذا؟}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبوضع $x - 2 = 5 \tan\theta$
</div>

$$\therefore x = 5 \tan\theta + 2 = g(\theta)$$

$$g'(\theta) = 5 \sec^2\theta$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وعندما $x = 2$ ، فإن:
</div>

$$5 \tan\theta + 2 = 2 \Rightarrow 5 \tan\theta = 0 \Rightarrow \tan\theta = 0 \Rightarrow \theta = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>147</strong> | الدرس 3-4 التكامل بالتعويض
</div>
<!-- PAGE_END_147 -->


<!-- PAGE_START_148 -->
### صفحة 148

<div dir="rtl" style="text-align: right; font-size: 16px;">
وعندما $x = 7$ ، فإن:
</div>

$$5 \tan\theta + 2 = 7 \Rightarrow 5 \tan\theta = 5 \Rightarrow \tan\theta = 1 \Rightarrow \theta = \frac{\pi}{4}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن الواضح أنه $\forall \theta \in [0, \frac{\pi}{4}]$ ، تكون $x \in [2, 7]$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ شروط نظرية التعويض متوفرة
</div>

$$\therefore \int_2^7 f(x) \, dx = \int_0^{\frac{\pi}{4}} f(g(\theta)) \, g'(\theta) \, d\theta$$

$$\Rightarrow \int_2^7 \frac{5}{x^2 - 4x + 9} \, dx = \int_0^{\frac{\pi}{4}} \left( \frac{5}{25 \tan^2\theta + 25} \right) (5 \sec^2\theta) \, d\theta$$

$$= \int_0^{\frac{\pi}{4}} \left( \frac{5}{25 \sec^2\theta} \right) (5 \sec^2\theta) \, d\theta$$

$$= \int_0^{\frac{\pi}{4}} d\theta$$

$$= (\theta) \Big|_0^{\frac{\pi}{4}}$$

$$= \frac{\pi}{4}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 6</strong>
<br>
احسب قيمة $\int_2^{2\sqrt{2}} \frac{\sqrt{x^2 - 4}}{x} \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<span style="color: red; font-weight: bold;">الحل</span>
</div>

$$\because f(x) = \frac{\sqrt{x^2 - 4}}{x}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبوضع $x = g(\theta) = 2 \sec\theta$
</div>

$$\therefore g'(\theta) = 2 \tan\theta \sec\theta$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وعندما $x = 2$ ، فإن:
</div>

$$2 \sec\theta = 2 \Rightarrow \sec\theta = 1 \Rightarrow \theta = 0$$

---

<div dir="rtl" style="text-align: right; font-size: 14px; margin-top: 20px;">
148 الفصل 4 التكامل المحدد
</div>
<!-- PAGE_END_148 -->


<!-- PAGE_START_149 -->
### صفحة 149

<div dir="rtl" style="text-align: right; font-size: 16px;">
وعندما $x = 2\sqrt{2}$ ، فإن:
</div>

$$2 \sec\theta = 2\sqrt{2} \Rightarrow \sec\theta = \sqrt{2} \Rightarrow \theta = \frac{\pi}{4}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن الواضح أنه $\forall \theta \in \left[ 0, \frac{\pi}{4} \right]$ ، تكون $x \in [2, 2\sqrt{2}]$<br>
$\because$ شروط نظرية التعويض متوافرة
</div>

$$\therefore \int_{2}^{2\sqrt{2}} f(x) \, dx = \int_{0}^{\frac{\pi}{4}} f(g(\theta)) \, g'(\theta) \, d\theta$$

$$\Rightarrow \int_{2}^{2\sqrt{2}} \frac{\sqrt{x^2 - 4}}{x} \, dx = \int_{0}^{\frac{\pi}{4}} \frac{\sqrt{4\sec^2\theta - 4}}{2\sec\theta} (2\tan\theta \sec\theta) \, d\theta$$

$$= \int_{0}^{\frac{\pi}{4}} \frac{2\tan\theta}{2\sec\theta} (2\tan\theta \sec\theta) \, d\theta$$

$$= \int_{0}^{\frac{\pi}{4}} 2\tan^2\theta \, d\theta$$

$$= 2 \int_{0}^{\frac{\pi}{4}} (\sec^2\theta - 1) \, d\theta$$

$$= 2 (\tan\theta - \theta) \Big|_{0}^{\frac{\pi}{4}}$$

$$= 2 \left[ \left( \tan\frac{\pi}{4} - \frac{\pi}{4} \right) - (\tan 0 - 0) \right]$$

$$= 2 \left[ \left( 1 - \frac{\pi}{4} \right) - (0) \right]$$

$$= 2 - \frac{\pi}{2}$$

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>مثال 7:</strong> احسب قيمة $\int_{\frac{1}{\sqrt{3}}}^{1} \frac{8x^3}{\sqrt{4x^2 - 1}} \, dx$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<strong>الحل:</strong>
</div>

$$\because f(x) = \frac{8x^3}{\sqrt{4x^2 - 1}}$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وبوضع $x = g(\theta) = \frac{1}{2}\sec\theta$
</div>

$$\therefore g'(\theta) = \frac{1}{2}\tan\theta \sec\theta$$

<div dir="rtl" style="text-align: right; font-size: 16px;">
وعندما $x = \frac{1}{\sqrt{3}}$ ، فإن:
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px;">
<strong>149</strong> | الدرس 3-4: التكامل بالتعويض
</div>
<!-- PAGE_END_149 -->


<!-- PAGE_START_150 -->
### صفحة 150

$$ \frac{1}{2} \sec\theta = \frac{1}{\sqrt{3}} \Rightarrow \sec\theta = \frac{2}{\sqrt{3}} \Rightarrow \theta = \frac{\pi}{6} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
عندما $x = 1$ ، فإن:
</div>

$$ \frac{1}{2} \sec\theta = 1 \Rightarrow \sec\theta = 2 \Rightarrow \theta = \frac{\pi}{3} $$

<div dir="rtl" style="text-align: right; font-size: 16px;">
ومن الواضح أنه $\forall \theta \in \left[\frac{\pi}{6}, \frac{\pi}{3}\right]$ ، تكون $x \in \left[\frac{1}{\sqrt{3}}, 1\right]$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
$\because$ شروط نظرية التعويض متوفرة
</div>

$$ \therefore \int_{\frac{1}{\sqrt{3}}}^{1} f(x) \, dx = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} f(g(\theta)) \, g'(\theta) \, d\theta $$

$$ \Rightarrow \int_{\frac{1}{\sqrt{3}}}^{1} \frac{8x^3}{\sqrt{4x^2 - 1}} \, dx = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{8\left(\frac{1}{2} \sec\theta\right)^3}{\sqrt{\sec^2\theta - 1}} \left(\frac{1}{2} \sec\theta \tan\theta\right) d\theta $$

$$ = \frac{1}{2} \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sec^4\theta \tan\theta}{\tan\theta} \, d\theta $$

$$ = \frac{1}{2} \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sec^4\theta \, d\theta $$

$$ = \frac{1}{2} \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} (1 + \tan^2\theta) \sec^2\theta \, d\theta $$

$$ = \frac{1}{2} \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} (\sec^2\theta + \tan^2\theta \sec^2\theta) \, d\theta $$

$$ = \frac{1}{2} \left[ \tan\theta + \frac{1}{3} \tan^3\theta \right]_{\frac{\pi}{6}}^{\frac{\pi}{3}} $$

$$ = \frac{1}{2} \left[ \left(\tan\frac{\pi}{3} + \frac{1}{3} \tan^3\frac{\pi}{3}\right) - \left(\tan\frac{\pi}{6} + \frac{1}{3} \tan^3\frac{\pi}{6}\right) \right] $$

$$ = \frac{1}{2} \left[ \left(\sqrt{3} + \left(\frac{1}{3}\right)(3\sqrt{3})\right) - \frac{1}{\sqrt{3}} - \left(\frac{1}{3}\right)\left(\frac{1}{3\sqrt{3}}\right) \right] $$

$$ = \frac{22\sqrt{3}}{27} $$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
<b>150</b> &nbsp;&nbsp;&nbsp;&nbsp; الفصل 4: التكامل المحدد
</div>
<!-- PAGE_END_150 -->


<!-- PAGE_START_151 -->
### صفحة 151

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h2>تمارين 3-4</h2>

احسب قيمة كُلٍّ من التكاملات الآتية:
</div>

$$\int_{0}^{3} \sqrt{9 - x^2} \, dx \tag{1}$$

$$\int_{\frac{1}{3}}^{\frac{2}{3}} \sqrt{4 - 9x^2} \, dx \tag{2}$$

$$\int_{2}^{2\sqrt{3}} \frac{1}{\sqrt{16 - x^2}} \, dx \tag{3}$$

$$\int_{1}^{\sqrt{2}} \frac{x^2}{\sqrt{4 - x^2}} \, dx \tag{4}$$

$$\int_{\frac{1}{4}}^{\frac{1}{2}} \frac{\sqrt{1 - 4x^2}}{x^2} \, dx \tag{5}$$

$$\int_{0}^{\frac{5}{4}} \frac{1}{16x^2 + 25} \, dx \tag{6}$$

$$\int_{\frac{\sqrt{3}}{2}}^{\frac{3\sqrt{3}}{2}} \frac{\sqrt{4x^2 + 9}}{x^4} \, dx \tag{7}$$

$$\int_{2\sqrt{3}}^{6} \frac{1}{x\sqrt{x^2 - 9}} \, dx \tag{8}$$

$$\int_{\frac{1}{3}}^{\frac{2}{3}} x^3 \sqrt{9x^2 - 1} \, dx \tag{9}$$

---

<div dir="rtl" style="text-align: right; font-size: 14px;">
الدرس 3-4 التكامل بالتعويض | 151
</div>
<!-- PAGE_END_151 -->


<!-- PAGE_START_152 -->
### صفحة 152

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>اختبار الفصل 4</b>
<br><br>
<b>احسب قيمة كلِّ من التكاملات الآتية:</b>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">

1. $$\int_{5}^{7} (x - 5)^6 \, dx$$

2. $$\int_{\frac{1}{\sqrt{2}}}^{1} x \sqrt{1 - x^2} \, dx$$

3. $$\int_{1}^{4} \frac{1}{x^2} \sqrt{1 - \frac{1}{x}} \, dx$$

4. $$\int_{4}^{5} (u^2 - 8u + 16)^3 \, du$$

5. $$\int_{4}^{6} (2 + |u - 2|) \, du$$

6. $$\int_{-1}^{3} (z |z|) \, dz$$

7. $$\int_{-2}^{-1} \left( \frac{|x|}{x} - 3 \right) dx$$

8. $$\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \frac{27}{\tan^5 x \sin^2 x} \, dx$$

9. $$\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} 2 \tan u \sec^2 u \, du$$

10. $$\int_{0}^{\frac{\pi}{4}} \frac{4 \tan u}{1 + \cos 2u} \, du$$

11. $$\int_{0}^{\frac{\pi}{2}} \frac{\sin^3 x - \cos^3 x}{\sin x - \cos x} \, dx$$

12. $$\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{\sin 4z}{\cos 2z} \, dz$$

13. $$\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} \frac{dx}{1 - \cos x}$$

</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>14</b> أثبت أن:
$$\int_{0}^{\frac{\pi}{4}} (\cos^2 x - \sin^2 x) \, dx = \int_{0}^{\frac{\pi}{4}} 2 \sin x \cos x \, dx$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>15</b> إذا كان:
$$\int_{0}^{b} \cos^2 u \sin u \, du = \frac{1}{3} , \quad b \in [0, \pi]$$
فأوجد قيمة $b$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>16</b> إذا كان:
$$\int_{-2}^{b} f(x) \, dx = 5 , \quad \int_{b}^{-2} (f(x) - 2) \, dx = 7$$
فأوجد قيمة $b$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 14px; color: #555;">
الفصل 4: التكامل المحدد | 152
</div>
<!-- PAGE_END_152 -->


<!-- PAGE_START_153 -->
### صفحة 153

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>17</b> إذا كان:
$$\int_0^3 n (x + 1)^{n-1} dx = 15$$
فأوجد قيمة $n$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>18</b> أوجد مساحة سطح المنطقة المحصورة بين المحور $x$ ومنحنى $f(x) = \sqrt{x}$ في الفترة $[0, 4]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>19</b> أوجد مساحة سطح المنطقة المحصورة بين المحور $x$ ومنحنى الدالة:
$$y = \cos 2x + \sin 2x$$
في الفترة $\left[0, \frac{\pi}{4}\right]$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>20</b> أوجد مساحة سطح المنطقة المحصورة بين منحنى الدالة $y = x^2 + 4$، والمستقيم $2x - y + 7 = 0$.
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>21</b> أوجد مساحة سطح المنطقة المحصورة بين منحنيي الدالتين:
$$y = x^2 - 6x + 9$$
$$y = 1 + 4x - x^2$$
</div>

<hr>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>احسب قيمة كلٍّ من التكاملات الآتية:</b>
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>22</b>
$$\int_0^4 \frac{dx}{x^2 + 16}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>23</b>
$$\int_1^2 \frac{\sqrt{x^2 - 1}}{x} dx$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>24</b>
$$\int_0^1 \frac{1}{\sqrt{2 - x^2}} dx$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>25</b>
$$\int_{\sqrt{2}}^{\frac{2}{\sqrt{3}}} \frac{dx}{x^2 \sqrt{x^2 - 1}}$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>26</b>
$$\int_0^{\frac{5}{2}} \frac{x^2}{\sqrt{25 - x^2}} dx$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>27</b>
$$\int_0^1 \frac{x^3}{\sqrt{x^2 + 1}} dx$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>28</b>
$$\int_0^{5\sqrt{2}} \frac{x^2}{\sqrt{100 - x^2}} dx$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>29</b>
$$\int_1^{\sqrt{3}} \frac{\sqrt{4 - x^2}}{x^2} dx$$
</div>

<div dir="rtl" style="text-align: right; font-size: 16px;">
<b>30</b>
$$\int_0^3 \frac{x^2}{x^2 + 9} dx$$
</div>

<br>

<div dir="rtl" style="text-align: right; font-size: 16px;">
153 اختبار الفصل
</div>
<!-- PAGE_END_153 -->


<!-- PAGE_START_154 -->
### صفحة 154

<div dir="rtl" style="text-align: right; font-size: 16px;">
<div style="background-color: #2e8b57; color: white; padding: 5px 15px; display: inline-block; border-radius: 5px; font-weight: bold; margin-bottom: 10px;">الصيغ</div>
</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="background-color: #5b9bd5; color: white; text-align: center; padding: 8px; border-radius: 5px; margin-top: 10px;">المتطابقات المثلثية</h3>

| الصيغة (2) | الصيغة (1) | اسم المتطابقة |
| :---: | :---: | :---: |
| $\cot \theta = \frac{\cos \theta}{\sin \theta}$ | $\tan \theta = \frac{\sin \theta}{\cos \theta}$ | **المتطابقات النسبية** |
| $\sin \theta = \frac{1}{\csc \theta}$ <br> $\csc \theta = \frac{1}{\sin \theta}$ | $\cos \theta = \frac{1}{\sec \theta}$ <br> $\sec \theta = \frac{1}{\cos \theta}$ | $\tan \theta = \frac{1}{\cot \theta}$ <br> $\cot \theta = \frac{1}{\tan \theta}$ | **متطابقات المقلوب** |
| $\cot^2 \theta + 1 = \csc^2 \theta$ | $\tan^2 \theta + 1 = \sec^2 \theta$ | $\sin^2 \theta + \cos^2 \theta = 1$ | **متطابقات فيثاغورس** |
| $\sec \theta = \csc \left(\frac{\pi}{2} - \theta\right)$ <br> $\csc \theta = \sec \left(\frac{\pi}{2} - \theta\right)$ | $\tan \theta = \cot \left(\frac{\pi}{2} - \theta\right)$ <br> $\cot \theta = \tan \left(\frac{\pi}{2} - \theta\right)$ | $\sin \theta = \cos \left(\frac{\pi}{2} - \theta\right)$ <br> $\cos \theta = \sin \left(\frac{\pi}{2} - \theta\right)$ | **متطابقات الزاويتين المتتامتين** |
| $\tan(-\theta) = -\tan \theta$ <br> $\cot(-\theta) = -\cot \theta$ | $\cos(-\theta) = \cos \theta$ <br> $\sec(-\theta) = \sec \theta$ | $\sin(-\theta) = -\sin \theta$ <br> $\csc(-\theta) = -\csc \theta$ | **متطابقات الدوال الزوجية أو الفردية** |
| $\cos(\alpha - \beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta$ <br> $\sin(\alpha - \beta) = \sin \alpha \cos \beta - \cos \alpha \sin \beta$ <br> $\tan(\alpha - \beta) = \frac{\tan \alpha - \tan \beta}{1 + \tan \alpha \tan \beta}$ | $\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$ <br> $\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$ <br> $\tan(\alpha + \beta) = \frac{\tan \alpha + \tan \beta}{1 - \tan \alpha \tan \beta}$ | **متطابقات المجموع والفرق** |
| $\cos 2\theta = 1 - 2 \sin^2 \theta$ | $\cos 2\theta = 2 \cos^2 \theta - 1$ <br> $\tan 2\theta = \frac{2 \tan \theta}{1 - \tan^2 \theta}$ | $\cos 2\theta = \cos^2 \theta - \sin^2 \theta$ <br> $\sin 2\theta = 2 \sin \theta \cos \theta$ | **متطابقات ضعف الزاوية** |
| $\tan \frac{\theta}{2} = \pm \sqrt{\frac{1 - \cos \theta}{1 + \cos \theta}}$ | $\cos \frac{\theta}{2} = \pm \sqrt{\frac{1 + \cos \theta}{2}}$ | $\sin \frac{\theta}{2} = \pm \sqrt{\frac{1 - \cos \theta}{2}}$ | **متطابقات نصف الزاوية** |

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="background-color: #5b9bd5; color: white; text-align: center; padding: 8px; border-radius: 5px; margin-top: 10px;">العمليات على الدوال</h3>

| القانون | العملية | القانون | العملية |
| :---: | :---: | :---: | :---: |
| $(f \cdot g)(x) = f(x) \cdot g(x)$ | **الضرب** | $(f + g)(x) = f(x) + g(x)$ | **الجمع** |
| $\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}, \quad g(x) \neq 0$ | **القسمة** | $(f - g)(x) = f(x) - g(x)$ | **الطرح** |
| | | $[f \circ g](x) = f[g(x)]$ | **تركيب دالتين** |

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<h3 style="background-color: #5b9bd5; color: white; text-align: center; padding: 8px; border-radius: 5px; margin-top: 10px;">النهايات</h3>

| القانون | اسم الخاصية |
| :---: | :---: |
| $\lim_{x \to c} [f(x) + g(x)] = \lim_{x \to c} f(x) + \lim_{x \to c} g(x)$ | **خاصية الجمع** |
| $\lim_{x \to c} [f(x) - g(x)] = \lim_{x \to c} f(x) - \lim_{x \to c} g(x)$ | **خاصية الفرق** |
| $\lim_{x \to c} [k \cdot f(x)] = k \cdot \lim_{x \to c} f(x)$ | **خاصية الضرب في عدد حقيقي** |
| $\lim_{x \to c} [f(x) \cdot g(x)] = \lim_{x \to c} f(x) \cdot \lim_{x \to c} g(x)$ | **خاصية الضرب** |
| $\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\lim_{x \to c} f(x)}{\lim_{x \to c} g(x)}, \quad \lim_{x \to c} g(x) \neq 0$ | **خاصية القسمة** |
| $\lim_{x \to c} [f(x)]^n = \left[\lim_{x \to c} f(x)\right]^n$ | **خاصية القوة** |
| $\lim_{x \to c} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to c} f(x)}, \quad \lim_{x \to c} f(x) > 0$ | **خاصية الجذر النوني** |

<br>

| السرعة المتجهة اللحظية | السرعة المتجهة المتوسطة |
| :---: | :---: |
| $v(t) = \lim_{h \to 0} \frac{f(t + h) - f(t)}{h}$ | $v_{\text{avg}} = \frac{f(b) - f(a)}{b - a}$ |

</div>

---

<div dir="rtl" style="text-align: right; font-size: 16px;">
<table width="100%" style="border: none; margin-top: 20px;">
  <tr>
    <td style="text-align: right; border: none;"><strong>154</strong> الصيغ والرموز</td>
    <td style="text-align: left; border: none;">البرهان والرموز <strong>154</strong></td>
  </tr>
</table>
</div>
<!-- PAGE_END_154 -->
