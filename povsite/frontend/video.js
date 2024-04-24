// Создание фигуры
const shape = new fabric.Rect({
    left: 0,
    top: 0,
    width: 500,
    height: 300,
    fill: 'white',
    stroke: 'black',
    strokeWidth: 2,
   });
   
   // Добавление фигуры на холст
   const canvas = new fabric.Canvas('canvas');
   canvas.add(shape);
   
   // Создание видео
   const video = document.getElementById('video');
   video.play();
   // Анимация фигуры
   shape.on('mouse:over', function () {
    shape.scaleToHeight(1.2);
   });
   
   shape.on('mouse:out', function () {
    shape.scaleToHeight(1);
   });
   
   // Анимация видео
   video.addEventListener('timeupdate', function () {
    const currentTime = video.currentTime;
    const duration = video.duration;
   
    if (currentTime >= duration) {
    video.currentTime = 0;
    }
   });