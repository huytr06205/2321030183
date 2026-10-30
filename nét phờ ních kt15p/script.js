var danhSachVid = [{
        id: 1,
        ten: "gánh mẹ",
        duongDanAnh: "../",
        duongDanYoutube: "https://www.youtube.com/embed/RVP5N4QXHeQ?si=c7JeRkndITvvbtkW"
    },
    {
        id: 2,
        ten: "sầu tím thiệp hồng",
        duongDanAnh: "",
        duongDanYoutube: "https://www.youtube.com/embed/RVP5N4QXHeQ?si=c7JeRkndITvvbtkW"

    },
    {
        id: 3,
        ten: "sau tim thiep hong",
        duongDanAnh: "sầu tím thiệp hồng",
        duongDanYoutube: "https://www.youtube.com/embed/RVP5N4QXHeQ?si=c7JeRkndITvvbtkW"

    },
    {
        id: 4,
        ten: "chuyện người con gái",
        duongDanAnh: "",
        duongDanYoutube: "https://www.youtube.com/embed/RVP5N4QXHeQ?si=c7JeRkndITvvbtkW"

    },
    {
        id: 5,
        ten: "bột ngô dang răng to",
        duongDanAnh: "",
        duongDanYoutube: "hhttps://www.youtube.com/embed/RVP5N4QXHeQ?si=c7JeRkndITvvbtkW"

    },
];

function chonPhim(id) {
    for (let i = 0; i < danhSachVid.length; i++) {
        if (danhSachVid[i].id == id) {
            document.getElementsByClassName("video")[0].src = danhSachVid[i].duongDanYoutube
        }
    }

}