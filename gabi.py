<!DOCTYPE html>
<html>
<head>
    <title>Рожден ден пожелание за Габи</title>
    <style>
        body {
            background-color: #ffeb3b; /* Променя цвета на фона на по-жълт */
            text-align: center; /* Центрира текста */
            font-family: Arial, sans-serif; /* Задава основния шрифт на страницата */
            margin: 0; /* Премахва стандартния маргин */
            padding: 0; /* Премахва стандартния падинг */
            overflow: hidden; /* Скрива скролбара */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .book {
            width: 80vw;
            height: 80vh;
            position: relative;
            perspective: 1000px;
        }
        .page {
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0;
            left: 0;
            background-color: #ffeb3b;
            backface-visibility: hidden;
            transform-style: preserve-3d;
            transition: transform 1s;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 20px;
            box-sizing: border-box;
        }
        .page-content {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100%;
            padding: 20px;
            box-sizing: border-box;
            text-align: center;
        }
        h1 {
            color: #333; /* Променя цвета на текста на тъмносив, за по-добра четимост */
            font-size: 2em; /* Задава размера на шрифта */
            font-weight: bold; /* Прави текста по-дебел */
        }
        p {
            color: #333; /* Променя цвета на текста на тъмносив, за по-добра четимост */
            font-size: 1.5em; /* Задава размера на шрифта */
            font-weight: bold; /* Прави текста по-дебел */
            margin: 20px 0; /* Добавя отстояние между параграфите */
        }
        .media-item {
            width: 80%; /* Задава ширината на всеки елемент */
            max-height: 80%; /* Задава максимална височина за елементите */
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .media-item img, .media-item video {
            max-width: 100%;
            max-height: 100%;
            width: auto;
            height: auto;
        }
        .nav-buttons {
            position: absolute;
            bottom: 20px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 20px;
        }
        .nav-buttons button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .page1 {
            z-index: 3;
        }
        .page2 {
            z-index: 2;
            transform: rotateY(180deg);
        }
        .page3 {
            z-index: 1;
            transform: rotateY(180deg);
        }
        .page.flip {
            transform: rotateY(-180deg);
        }
    </style>
</head>
<body>

<div class="book">
    <div id="page1" class="page page1">
        <div class="page-content">
            <h1>Честит рожден ден, Габче!</h1>
            <p>Пожелавам ти много здраве, щастие, любов, късмет и успех във всяко нещо, което правиш.</p>
            <p>Нека имаш добри и верни приятели, уникални и незабравими моменти с любимите си хора, безброй усмивки и сбъднати мечти!</p>
            <p>Бъди винаги толкова лъчезарна, всеотдайна, добра (само с определени хора), готина, забавна и щура (в добрия смисъл, разбира се).</p>
            <p>Никога не се променяй, защото си една на 8009427207!</p>
            <p>Love you to JADES-GS-z14-0/GN-z11 (двете най-далечни галактики открити до сега) and back.</p>
        </div>
    </div>

    <div id="page2" class="page page2">
        <div class="page-content">
            <div class="media-item">
                <img src="Screenshot_20240616_151719.jpg" alt="Sunflowers for my sunflower">
            </div>
        </div>
    </div>

    <div id="page3" class="page page3">
        <div class="page-content">
            <div class="media-item">
                <video controls>
                    <source src="Happy birthday it’s your birthday lemon.mp4" type="video/mp4">
                    Вашият браузър не поддържа вградени видеоклипове.
                </video>
            </div>
        </div>
    </div>
</div>

<div class="nav-buttons">
    <button onclick="prevPage()">Назад</button>
    <button onclick="nextPage()">Напред</button>
</div>

<script>
    let currentPage = 1;
    const totalPages = 3;

    function showPage(page) {
        for (let i = 1; i <= totalPages; i++) {
            const pageElement = document.getElementById('page' + i);
            if (i < page) {
                pageElement.style.transform = 'rotateY(-180deg)';
            } else {
                pageElement.style.transform = 'rotateY(0deg)';
            }
        }
    }

    function nextPage() {
        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    }

    function prevPage() {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    }
</script>

</body>
</html>
