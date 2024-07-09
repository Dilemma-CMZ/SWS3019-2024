let list = document.getElementsByClassName("tit");
let titles = [], types = [];
for (let i = 0; i < list.length; i++) {
    if (list[i].firstElementChild != null) {
        let ch = list[i].firstElementChild.firstElementChild;
        if (ch != null) {
            let tagParent = list[i].parentNode.children[2];
            if (tagParent != null) {
                let tag = tagParent.firstElementChild.firstElementChild;
                if (tag != null) {
                    if (typeof ch.textContent != "undefined" && typeof tag.textContent != "undefined") {
                        titles.push('"' + ch.textContent + '"');
                        // types.push('"' + tag.textContent + '"');
                    }
                }
            }
        }
    }
}
console.log(titles.toString());
// console.log(types.toString());