from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

SECTIONS = {
    'hayoc_lezou': {
        'title': 'Հայոց լեզու',
        'title_ru': 'Հայոց լեզու',
        'emoji': '🇦🇲',
        'color': '#e74c3c',
        'pages': '3–12',
        'content': """
<h3>Հարադրավոր բաղադրյալ հատուկ անվան բոլոր բաղադրիչները (բացի շաղկապներից) սկսվում են մեծատառով.</h3>

<h4>Անձնանուններ</h4>

<div class="letter-section">
<div class="letter">Ա</div>
<ul>
<li>Ակսել Բակունց</li><li>Ալիսիա Կիրակոսյան</li><li>Անտոն Խիժնյակ</li>
<li>Անտուան Մեյե</li><li>Արամ Խաչատրյան</li><li>Առնո Բաբաջանյան</li>
<li>Արշալույս Մարգարյան</li><li>Ազատ Վշտունի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Բ</div>
<p class="empty-note">(—)</p>
</div>

<div class="letter-section">
<div class="letter">Գ</div>
<ul>
<li>Գեղամ Սարյան</li><li>Գևորգ Էմին</li><li>Գրիգոր Լուսավորիչ</li><li>Գրիգոր Նարեկացի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Դ</div>
<ul><li>Դավիթ Զաքարյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Է</div>
<ul><li>Էդուարդ Մեժելայտիս</li></ul>
</div>

<div class="letter-section">
<div class="letter">Թ</div>
<ul><li>Թոմ Կրոնին</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ժ</div>
<ul><li>Ժամկոչյան Պերճ</li></ul>
</div>

<div class="letter-section">
<div class="letter">Խ</div>
<ul>
<li>Խորեն Պալյան</li><li>Հենրիխ Հյուբշման</li><li>Խիժնյակ Անտոն</li>
<li>Խաչատրյան Արամ</li><li>Խորենացի Մովսես</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Լ</div>
<ul><li>Լուսինե Զաքարյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Մ</div>
<ul>
<li>Մարտիրոս Սարյան</li><li>Մեսրոպ Մաշտոց</li><li>Մխիթար Գոշ</li>
<li>Միխայիլ Մատուսովսկի</li><li>Մովսես Խորենացի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Ն</div>
<ul><li>Նաիրի Զարյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Պ</div>
<ul>
<li>Պարույր Սևակ</li><li>Պետրոս Դուրյան</li><li>Պերճ Ժամկոչյան</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Ս</div>
<ul>
<li>Սիլվա Կապուտիկյան</li><li>Ստեփան Զորյան</li><li>Հովհաննես Շիրազ</li>
<li>Սվետլանա Նավասարդյան</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Տ</div>
<ul>
<li>Տիգրան Մանսուրյան</li><li>Տոմաշևիչ Իոսիֆ</li>
<li>Տոմաշևսկայա Ելենա</li><li>Տոմաշևսկայա Վերոնիկա</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Վ</div>
<ul>
<li>Վարդան Այգեկցի</li><li>Վահագն Դավթյան</li><li>Վերոնիկա Տոմաշևսկայա</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Հ</div>
<ul>
<li>Հովհաննես Թումանյան</li><li>Հովհաննես Իսակով</li><li>Հենրիխ Հյուբշման</li>
<li>Հրաչյա Աճառյան</li><li>Հակոբ Կոջոյան</li><li>Հաբեթ Զաքարյան</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Ջ</div>
<ul><li>Ջոնաթան Սվիֆթ</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ռ</div>
<ul><li>Ռոմանոս Մելիքյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Մ</div>
<ul><li>Մարգար Մարգարյան</li></ul>
</div>

<hr class="section-divider">
<h4>Աշխարհագրական տեղանուններ</h4>
<h5>Պետությունների և դրանց միությունների անուններում</h5>

<div class="letter-section">
<div class="letter">Ա</div>
<ul><li>Ամերիկայի Միացյալ Նահանգներ</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ի</div>
<ul><li>Իրանի Իսլամական Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Լ</div>
<ul><li>Լեռնային Ղարաբաղի Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ն</div>
<ul><li>Նախիջևանի Ինքնավար Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Հ</div>
<ul><li>Հայաստանի Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ս</div>
<ul><li>Սանկտ Պետերբուրգ</li></ul>
</div>

<hr class="section-divider">
<h5>Լրացումից և լրացյալից կազմված անուններ</h5>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ախթալայի ամրոց</li><li>Աքոռիի լեռնային սարավանդ</li>
<li>Արամ նահապետ</li><li>Արայի լեռներ</li>
<li>Արարատյան դաշտ</li><li>Արեգունի լեռնաշղթա</li><li>Արտանիշի թերակղզի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բարեբեր գետ</li></ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul>
<li>Գայանեի տաճար</li><li>Գեղամա սարեր</li>
<li>Գետիկի ավազան</li><li>Գետիկի հովիտ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul>
<li>Դեբեդի ձոր</li><li>Դիլիջան ազգային այգի</li>
<li>Դրախտիկ գետ</li><li>Դսեղի լեռնային սարավանդ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Զ</div>
<ul><li>Զաքարե զորավար</li></ul>
</div>

<div class="letter-section"><div class="letter">Թ</div>
<ul>
<li>Թիֆլիսի ռեալական դպրոց</li><li>Թումանյան կայարան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ժ</div>
<ul><li>Ժանգոտ լիճ</li></ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լոռվա դաշտ</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մշո Սուրբ Կարապետ վանք</li><li>Միափորի լեռնանցք</li></ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul>
<li>Պարզ լիճ</li><li>Պետերբուրգի կայսերական թատրոն</li>
<li>Պրուսովի անվան արվեստանոց</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Փ</div>
<ul>
<li>Փամբակի գոգահովիտ</li><li>Փամբակի լեռներ</li><li>Փամբակի լեռնաշղթա</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սանահինի կամուրջ</li><li>Սարդարապատի հուշահամալիր</li>
<li>Սևանի ավազան</li><li>Սևանի լեռնանցք</li><li>Սոսյաց անտառ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Տ</div>
<ul><li>Տաթևի վանք</li><li>Տիրի տաճար</li></ul>
</div>

<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խալդիի դարպաս</li><li>Խաղաղ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Ք</div>
<ul><li>Քաշաթաղ լեռնագագաթ</li><li>Քառասնից մանկան վանք</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul>
<li>Կայան բերդ</li><li>Կասպից ծով</li><li>Կովկասյան ծովափ</li><li>Կուրի ավազան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հաղպատի վանք</li><li>Հյուսիսկովկասյան ռազմաճակատ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ճ</div>
<ul><li>Ճամբարակի գոգահովիտ</li><li>Ճամբարակի լեռնանցք</li></ul>
</div>

<hr class="section-divider">
<h5>Ստեղծագործությունների անուններ</h5>
<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ա. Խաչատրյան «Գայանե» բալետ</li>
<li>Ա. Խաչատրյան «Սուսերով պար»</li>
</ul>
</div>

<hr class="section-divider">
<h5>Պետության կողմից շնորհվող շքանշանների անուններ</h5>
<div class="letter-section"><div class="letter">Խ</div>
<ul>
<li>ԽՍՀՄ պետական մրցանակ</li><li>Խորհրդային Միության հերոս</li>
</ul>
</div>

<hr class="section-divider">
<h5>Այլ կանոններ</h5>
<div class="rule-box">
<p>Հայկական բառը երբեմն հատուկ անվան առաջին բաղադրիչ է</p>
</div>
<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայկական պար լեռնաշղթա</li><li>Հայկական Տավրոս</li></ul>
</div>

<div class="rule-box">
<p>Տեղանուններում հաճախ հատուկ անվան առաջին բաղադրիչ են՝ Արևելյան, Մեծ, Մերձ, Նոր, Փոքր...</p>
</div>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արևելյան Հայաստան</li></ul>
</div>
<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Մասիս</li><li>Մերձավոր Արևելք</li></ul>
</div>
<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նոր Ջուղա</li></ul>
</div>
<div class="letter-section"><div class="letter">Փ</div>
<ul><li>Փոքր Կովկաս</li><li>Փոքր Մասիս</li><li>Փոքր Մհեր</li><li>Փոքր Սևան</li></ul>
</div>

<div class="rule-box">
<p>Տիեզերական մարմինների և համաստեղությունների անուններում առաջին բաղադրիչն է մեծատառով</p>
</div>
<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արեգակնային համակարգ</li></ul>
</div>
<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լուսնի խավարում</li></ul>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> Մայր բառը՝ մայր քաղաք, մայր տաճար, մայր բուհ — սովորական որոշիչ է, գրվում է փոքրատառով։ Միայն Մայր Աթոռ Սուրբ Էջմիածնի դեպքում՝ մեծատառով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> Եկեղեցիների, վանքերի անվանումներում, երբ Սուրբ բառը առաջին բաղադրիչն է, գրվում է մեծատառով։</p>
</div>
<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայոց Սբ. Ստեփանոս վանք</li></ul>
</div>

<div class="rule-box">
<p><strong>Աստված բառը</strong> կարելի է մեծատառով գրել, երբ վերաբերում է քրիստոնյաների պաշտած Աստծուն, բայց փոքրատառով՝ մնացած դեպքերում։</p>
</div>
<div class="letter-section"><div class="letter">Տ</div>
<ul><li>Տիր աստված</li></ul>
</div>

<div class="rule-box"><p>Ավանդական գրությամբ գծիկով գրվող անուններ</p></div>
<div class="letter-section"><div class="letter">Ն</div><ul><li>Նար-Դոս</li></ul></div>
<div class="letter-section"><div class="letter">Ս</div><ul><li>Սայաթ-Նովա</li></ul></div>
"""
    },
    'hay_grakanutyan': {
        'title': 'Հայ գրականություն',
        'title_ru': 'Հայ գրականություն',
        'emoji': '📚',
        'color': '#8e44ad',
        'pages': '13–21',
        'content': """
<h3>Հարադրավոր բաղադրյալ հատուկ անվան բոլոր բաղադրիչները (բացի շաղկապներից) սկսվում են մեծատառով։</h3>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ավետիք Իսահակյան</li><li>Արամ Խաչատրյան</li><li>Ակսել Բակունց</li>
<li>Ալեքսանդր Պուշկին</li><li>Ալեքսանդր Բլոկ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գաբրիել Սունդուկյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դանիել Վարուժան</li><li>Դերենիկ Դեմիրճյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լևոն Շանթ</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հովհաննես Թումանյան</li><li>Հովհաննես Հովհաննիսյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ղ</div>
<ul><li>Ղևոնդ Ալիշան</li><li>Ղազարոս Աղայան</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեսրոպ Մաշտոց</li><li>Մուրադ-Ռափայելյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նար-Դոս</li><li>Նաիրի Զարյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սուրբ Գրիգոր Լուսավորիչ</li><li>Ստեֆան Ցվայգ</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վահան Թեքեյան</li><li>Վասիլի Շուկշին</li><li>Վիկտոր Հյուգո</li><li>Վահան Տերյան</li>
</ul>
</div>

<hr class="section-divider">
<h4>Պատմական երկրանունների միայն առաջին բաղադրիչն է մեծատառով գրվում</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արտաշեսյան թագավորություն</li><li>Արշակունյաց թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բագրատունիների թագավորություն</li><li>Բյուզանդական կայսրություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Երվանդունիների թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կիլիկիայի թագավորություն</li><li>Կարսի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Հայքի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սյունիքի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վասպուրականի թագավորություն</li><li>Վանի թագավորություն</li></ul>
</div>

<hr class="section-divider">
<h4>Տեղանուններում առաջին բաղադրիչը</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արևելյան Հայաստան</li><li>Արևմտյան Հայաստան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իսպանիայի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խաղաղ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կարմիր ծով</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հին աշխարհ</li><li>Հյուսիսային սառուցյալ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Բրիտանիա</li><li>Մեծ Մասիս</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նոր աշխարհ</li></ul>
</div>

<hr class="section-divider">
<h4>Անիի միջնաբերդ, լրացուցիչ մականուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Անիի միջնաբերդ</li><li>Աթենքի միջնաբերդ</li><li>Անդրեաս գնդապետ</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>դյուցազն Վարդան</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայկ նահապետ</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վազգեն սպարապետ</li></ul>
</div>

<hr class="section-divider">
<h4>Սուրբ – եկեղեցու անվանումներում</h4>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սուրբ Գրիգոր Լուսավորիչ եկեղեցի</li>
<li>Սուրբ Թադևոս վանք</li>
<li>Սուրբ Աննա եկեղեցի</li>
<li>Սուրբ Մարիամ մայր տաճար</li>
</ul>
</div>

<hr class="section-divider">
<h4>Մականունով անուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արա Գեղեցիկ</li><li>Աշոտ Երկաթ</li></ul>
</div>
<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գայլ Վահան</li></ul>
</div>
<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դավիթ Անհաղթ</li></ul>
</div>
<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խոսրով Կոտակ</li></ul>
</div>
<div class="letter-section"><div class="letter">Ձ</div>
<ul><li>Ձախորդ Փանոս</li></ul>
</div>
<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Մհեր</li></ul>
</div>
"""
    },
    'hayoc_patmutyun': {
        'title': 'Հայոց պատմություն',
        'title_ru': 'История Армении',
        'emoji': '🏛️',
        'color': '#e67e22',
        'pages': '22–28',
        'content': """
<h3>Անձնանուններ</h3>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Աբգար V Ուքամա</li><li>Արտաշես Մեծ</li><li>Ավագ Ջալալյան</li>
<li>Ավետիք Բակունց</li><li>Ագաթանգեղոս</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վարդանանց պատերազմ</li>
<li>Վարդան Մամիկոնյան</li>
</ul>
</div>

<h4>«Հայկական քաղաքակրթությունը նոր շրջանում»</h4>
<div class="rule-box">
<p>Այս բառարանը ընդգրկում է Հայոց պատմության 11-րդ դասարանի դասագրքի հատուկ անունները։</p>
</div>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Աշոտ I Մեծ</li><li>Արշակ II</li><li>Արամ I</li>
<li>Արտաշես I</li><li>Արտաշես II</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul>
<li>Գանձակ</li><li>Գրիգորիս</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul>
<li>Դավիթ Անհաղթ</li><li>Դավիթ Սասունցի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul>
<li>Մեծ Մհեր</li><li>Մովսես Խորենացի</li><li>Մեսրոպ Մաշտոց</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Տ</div>
<ul>
<li>Տիգրան Մեծ</li><li>Տիգրանակերտ</li>
</ul>
</div>

<hr class="section-divider">
<h4>Աշխարհագրական տեղանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Հայաստանի Անկախություն</li><li>Արտաշատ</li><li>Արտաշես</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կարին (Էրզրում)</li><li>Կիլիկիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Հայք</li><li>Մասիս</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սասուն</li><li>Սևան</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վան</li><li>Վասպուրական</li></ul>
</div>
"""
    },
    'hamashkharhayin': {
        'title': 'Համաշխարհային պատմություն',
        'title_ru': 'Всемирная история',
        'emoji': '🌍',
        'color': '#27ae60',
        'pages': '29–42',
        'content': """
<h3>Հարադրավոր հատուկ անունների բոլոր բաղադրիչները գրվում են մեծատառով</h3>
<h4>Տեղանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Արևմտյան Հայաստան</li><li>Արևելյան Հայաստան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իսպանիայի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կարմիր ծով</li></ul>
</div>

<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խաղաղ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հին աշխարհ</li><li>Հյուսիսային սառուցյալ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Բրիտանիա</li><li>Մեծ Մասիս</li><li>Մեծ արջ</li></ul>
</div>

<div class="letter-section"><div class="letter">Փ</div>
<ul><li>Փոքր արջ</li></ul>
</div>

<hr class="section-divider">
<h4>Անձնանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ալեքսանդր Մակեդոնացի (Մեծ)</li><li>Արամուս</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բիսմարկ</li></ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գարիբալդի</li><li>Չինգիզ խան</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կլոդ Մոնե</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նապոլեոն</li><li>Նելսոն Մանդելա</li></ul>
</div>

<div class="letter-section"><div class="letter">Ռ</div>
<ul><li>Ռուսո</li><li>Ռոբեսպիեռ</li></ul>
</div>

<hr class="section-divider">
<h4>Պատմական պետություններ, կազմակերպություններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ավստրիական կայսրություն</li><li>Ասորական կայսրություն</li>
<li>Անտիկ աշխարհ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բրիտանական կայսրություն</li><li>Բրիտանիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Եվրոպական միություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ռ</div>
<ul><li>Ռուսական կայսրություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ֆ</div>
<ul><li>Ֆրանսիական հանրապետություն</li></ul>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների, միությունների անուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>«Ալյանս» – Դաշինք</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul>
<li>Կլոդ Մոնե – գեղեցիկ նկարներ</li>
</ul>
</div>
"""
    },
    'rusac_lezou': {
        'title': 'Ռուսաց լեզու',
        'title_ru': 'Ռուսաց լեզու',
        'emoji': '🇷🇺',
        'color': '#2980b9',
        'pages': '43–66',
        'content': """
<h3>Հարադրավոր հատուկ անունների բոլոր բաղադրիչները գրվում են մեծատառով</h3>
<h4>Անձնանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Անդրեյ Բելիյ</li><li>Ալեքսանդր Բլոկ</li><li>Ալեքսեյ Տոլստոյ</li>
<li>Աննա Ախմատովա</li><li>Անտոն Չեխով</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul>
<li>Բորիս Պաստեռնակ</li><li>Բորիս Խորոշիլով</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վլադիմիր Վիսոցկի</li><li>Վլադիմիր Մայակովսկի</li><li>Վլադիմիր Ռոզով</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul>
<li>Գորկի Մաքսիմ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul>
<li>Իվան Բունին</li><li>Իվան Տուրգենև</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul>
<li>Կոնստանտին Պաուստովսկի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul>
<li>Լեոնիդ Օսիպովիչ Պաստեռնակ</li>
<li>Լև Տոլստոյ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul>
<li>Մաքսիմ Գորկի</li>
<li>Մենդելեև</li><li>Միխայիլ Բուլգակով</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Օ</div>
<ul><li>Օլեգ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սերգեյ Եսենին</li><li>Սերգեյ Էֆրոն</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Տ</div>
<ul>
<li>Տատյանա</li><li>Տուրգենև Իվան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ֆ</div>
<ul><li>Ֆյոդոր Դոստոևսկի</li></ul>
</div>

<hr class="section-divider">
<h4>Մեսրոպ Մաշտոց</h4>
<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Մեսրոպ Մաշտոց</span><span class="lang-am">Մեսրոպ Մաշտոց</span></div>
<div class="bilingual-item"><span class="lang-ru">Վլադիմիր Ռոզով</span><span class="lang-am">Վլադիմիր Ռոզով</span></div>
</div>

<hr class="section-divider">
<h4>Աշխարհագրական անուններ</h4>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վոլգա</li><li>Վլադիվոստոկ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul>
<li>Դանկո</li><li>Հեռավոր Արևելք</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul>
<li>Կուբան</li><li>Կովկաս</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul>
<li>Մոսկվա</li><li>Միխայլովսկոյե</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սանկտ Պետերբուրգ</li><li>Սիբիր</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ֆ</div>
<ul>
<li>Գերմանիայի Դաշնային Հանրապետություն — ԳԴՀ</li>
</ul>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների անուններ</h4>

<div class="letter-section"><div class="letter">Բ</div>
<ul>
<li>«Սպիտակ գվարդիա»</li><li>«Կարամազով եղբայրները»</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>«Պատերազմ և խաղաղություն»</li><li>«Բալենու այգի»</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul>
<li>«Վայրէջք կատարեցին»</li><li>«Վոլոդյա Վիսոցկու մասին»</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>«Դոն Կիխոտ»</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>«Եվգենի Օնեգին»</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>«Ապուշ»</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>«Կապիտանի դուստրը»</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>«Վարպետը և Մարգարիտան»</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>«Եղջեր ու համառ»</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>«Քույրս՝ իմ կյանքը»</li><li>«Սառը աշուն»</li><li>«Ծեր Իզերգիլ»</li></ul>
</div>

<div class="letter-section"><div class="letter">Չ</div>
<ul><li>«Ճայը»</li></ul>
</div>

<div class="letter-section"><div class="letter">Յ</div>
<ul><li>«Փոս»</li></ul>
</div>

<div class="letter-section"><div class="letter">Ջ</div>
<ul><li>«Ջան»</li></ul>
</div>

<div class="letter-section"><div class="letter">Փ</div>
<ul><li>«Փոքրիկ զինվորը»</li></ul>
</div>

<hr class="section-divider">
<h4>Քերականական կանոններ</h4>

<div class="rule-box">
<p><strong>Կանոն 1:</strong> Ընդդիմություն — ընդհանուր անվանում։ Հասարակ գոյականները գրվում են փոքրատառով, եթե գործածվում են ընդհանուր իմաստով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն 2:</strong> Առաջին համաշխարհային պատերազմ։ Պատմական իրադարձությունների անունները գրվում են մեծատառով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն 3:</strong> Իտալացի։ Ազգությունների անունները հայերենում գրվում են փոքրատառով, իսկ անգլերենում՝ մեծատառով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն 4:</strong> Հայաստանի նախագահ։ Պաշտոնական անվանումներում պաշտոնները գրվում են մեծատառով։</p>
</div>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Առաջին համաշխարհային պատերազմ</li><li>Երկրորդ համաշխարհային պատերազմ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իտալացի</li></ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul><li>Հայաստանի նախագահ</li></ul>
</div>

<hr class="section-divider">
<h4>Հապավումների կանոններ</h4>

<div class="rule-box">
<p>Հապավումները կազմվում են ըստ ընդունված ձևի և գրվում են կրճատված, հստակ ձևով։</p>
</div>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>ԱՄՆ — Ամերիկայի Միացյալ Նահանգներ</li><li>ՄԲ — Մեծ Բրիտանիա</li><li>ՄԱԿ — Միավորված Ազգերի Կազմակերպություն</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>ՆԱՏՕ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>ԵՄ — Եվրոպական Միություն</li></ul>
</div>
"""
    },
    'angleren': {
        'title': 'Անգլերեն',
        'title_ru': 'Անգլերեն',
        'emoji': '🇬🇧',
        'color': '#1abc9c',
        'pages': '67–99',
        'content': """
<h3>Հարադրավոր հատուկ անունների բոլոր բաղադրիչները գրվում են մեծատառով</h3>
<h4>Անձնանուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Angela Merkel</span><span class="lang-am">Անժելա Մերկել</span></div>
<div class="bilingual-item"><span class="lang-en">Ardem Patapoutian</span><span class="lang-am">Արդեմ Պատափուտյան</span></div>
<div class="bilingual-item"><span class="lang-en">Betsy Ross</span><span class="lang-am">Բեթսի Ռոս</span></div>
<div class="bilingual-item"><span class="lang-en">David Julius</span><span class="lang-am">Դևիդ Ջուլիուս</span></div>
<div class="bilingual-item"><span class="lang-en">David Ogilvy</span><span class="lang-am">Դևիդ Օգիլվի</span></div>
<div class="bilingual-item"><span class="lang-en">Doctor Julius</span><span class="lang-am">Դոկտոր Ջուլիուս</span></div>
<div class="bilingual-item"><span class="lang-en">Doctor Park</span><span class="lang-am">Դոկտոր Պարկ</span></div>
<div class="bilingual-item"><span class="lang-en">Doctor Patapoutian</span><span class="lang-am">Դոկտոր Պատափուտյան</span></div>
<div class="bilingual-item"><span class="lang-en">Elizabeth 2nd</span><span class="lang-am">Ելիզավետա Երկրորդ</span></div>
<div class="bilingual-item"><span class="lang-en">Thomas Perlman</span><span class="lang-am">Թոմաս Պեռլման</span></div>
<div class="bilingual-item"><span class="lang-en">Srap Gevorgyan</span><span class="lang-am">Սրապ Գևորգյան</span></div>
</div>

<hr class="section-divider">
<h4>Աշխարհագրական անուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">South America</span><span class="lang-am">Հարավային Ամերիկա</span></div>
<div class="bilingual-item"><span class="lang-en">Japan</span><span class="lang-am">Ճապոնիա</span></div>
<div class="bilingual-item"><span class="lang-en">Brazil</span><span class="lang-am">Բրազիլիա</span></div>
<div class="bilingual-item"><span class="lang-en">Pacific Ocean</span><span class="lang-am">Խաղաղ օվկիանոս</span></div>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների անուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Ottoman Empire</span><span class="lang-am">Օսմանյան կայսրություն</span></div>
</div>

<hr class="section-divider">
<h4>Քերականական կանոններ</h4>

<div class="rule-box">
<p><strong>Կանոն 1:</strong> Ընդդիմություն՝ ընդհանուր անվանում։ Հասարակ գոյականները գրվում են փոքրատառով, երբ գործածվում են ընդհանուր իմաստով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն 2:</strong> Առաջին համաշխարհային պատերազմ։ Պատմական իրադարձությունների անունները գրվում են մեծատառով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն 3:</strong> Իտալացի։ Ազգությունների անունները հայերենում գրվում են փոքրատառով, իսկ անգլերենում՝ մեծատառով։</p>
</div>

<div class="rule-box">
<p><strong>Կանոն 4:</strong> Հայաստանի նախագահ։ Պաշտոնական անվանումներում պաշտոնները գրվում են մեծատառով։</p>
</div>

<div class="letter-section"><div class="letter">W</div>
<ul>
<li>Առաջին համաշխարհային պատերազմ</li>
<li>Երկրորդ համաշխարհային պատերազմ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">I</div>
<ul><li>Իտալացի</li></ul>
</div>

<div class="letter-section"><div class="letter">P</div>
<ul><li>Հայաստանի նախագահ</li></ul>
</div>

<hr class="section-divider">
<h4>Հապավումների կանոններ</h4>

<div class="rule-box">
<p>Հապավումները կազմվում են ըստ ընդունված ձևի և գրվում են կրճատված, հստակ ձևով։</p>
</div>

<div class="letter-section"><div class="letter">U</div>
<ul>
<li>ԱՄՆ — Ամերիկայի Միացյալ Նահանգներ</li>
<li>ՄԲ — Մեծ Բրիտանիա</li>
<li>ՄԱԿ — Միավորված Ազգերի Կազմակերպություն</li>
</ul>
</div>

<div class="letter-section"><div class="letter">N</div>
<ul><li>ՆԱՏՕ</li></ul>
</div>

<div class="letter-section"><div class="letter">E</div>
<ul><li>ԵՄ — Եվրոպական Միություն</li></ul>
</div>
"""
    }
}# Данные для блока "Ով է կազմել այս բառարանը" на главной странице
INTRO_DATA = {
    'compilers': ['Ռուբեն Թաթևոսյան', 'Անուն Ազգանուն 2', 'Անուն Ազգանուն 3'],
    'assignments': [
        ('Հայոց լեզու', 'Ռուբեն Թաթևոսյան'),
        ('Հայ գրականություն', 'Անուն Ազգանուն'),
        ('Հայոց պատմություն', 'Անուն Ազգանուն'),
        ('Համաշխարհային պատմություն', 'Անուն Ազգանուն'),
        ('Ռուսաց լեզու', 'Անուն Ազգանուն'),
        ('Անգլերեն', 'Անուն Ազգանուն')
    ],
    'editor': 'Խմբագրի Անունը',
    'supervisor': 'Նախագծի ղեկավար',
    'letter': 'Այս էլեկտրոնային բառարանը ստեղծվել է 11-րդ դասարանի նախագծային աշխատանքի շրջանակներում: Հուսով ենք՝ այն օգտակար կլինի բոլորին:'
}

@app.route('/')
def index():
    # Отдаем главную страницу, прокидываем секции и данные авторов
    return render_template('index.html', sections=SECTIONS, intro=INTRO_DATA)

@app.route('/section/<section_id>')
def section(section_id):
    # Если запрашивают несуществующую секцию
    if section_id not in SECTIONS:
        return "Էջը չի գտնվել (404 Not Found)", 404
    
    # Отдаем страницу конкретного предмета
    return render_template('section.html', 
                           section=SECTIONS[section_id], 
                           sections=SECTIONS, 
                           section_id=section_id)

if __name__ == '__main__':
    # host='0.0.0.0' нужен, чтобы сервак был доступен по локальной сети. 
    # Удобно, если запускаешь Flask прямо в Pydroid 3 на телефоне и хочешь посмотреть с компа.
    app.run(debug=True, host='0.0.0.0', port=5000)

