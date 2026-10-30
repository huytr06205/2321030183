var danhSachBaiHat = [{
    id: 1,
    ten: "Gánh mẹ",
    duongDanAnh: "",
    duongDanYoutube: "https://www.youtube.com/embed/cXpP9v3IQk8"
}, {
    id: 2,
    ten: "em ơi lâu đài tình ái",
    duongDanAnh: "../anh/anh 2.png",
    duongDanYoutube: "https://www.youtube.com/embed/OzOHyowIzgg"
}, {
    id: 3,
    ten: "đắp mộ",
    duongDanAnh: "../anh/anh 3.png",
    duongDanYoutube: "https://www.youtube.com/embed/emH2LgE-4SE"
}, {
    id: 4,
    ten: "BOMMAN",
    duongDanAnh: "../anh/anh 4.png",
    duongDanYoutube: "https://www.youtube.com/embed/CYLY7ZTg0Cs"
}, {
    id: 5,
    ten: "hoa phượng đỏ",
    duongDanAnh: "../anh/anh 5.png",
    duongDanYoutube: "https://www.youtube.com/embed/K5p09EGkQuU"
}];

function chonbai(id) {

    // Tìm bài hát theo ID
    var baiDuocChon = danhSachBaiHat.find(function(bai) {
        return bai.id == id;
    });

    // Nếu tìm thấy bài hát
    if (baiDuocChon) {

        // Lấy khung video
        var video = document.getElementById("video-banner");

        // Thay đổi video
        video.src = baiDuocChon.duongDanYoutube + "?autoplay=1";

    }
}