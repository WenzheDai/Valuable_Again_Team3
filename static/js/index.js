window.onload = function () {
    let hrefStr = window.location.href;
    let category = hrefStr.split('/')[3]
    console.log(category)
    const categoryList = ['Tableware', 'Food', 'Clothing', 'Device', 'Furniture']
    if (category === '') {
        $('#category-all').addClass('active')
    }else if (categoryList.includes(category)) {
        $("#category-"+category).addClass('active')
    }else {
        window.location.replace('')
    }
}