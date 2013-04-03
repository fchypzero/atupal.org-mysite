
function display_rss(data) {
    //alert(JSON.stringify(data));
    //console.log(JSON.stringify(data));
    rss_container = $("#rss_container")[0];
    //rss_container.removeChild();
    for (var i = 0; i < data.entries.length; ++ i) {
        div = document.createElement("div");
        div.class = "rss_container_div";
        div.id = "container_" + i.toString();

        h3 = document.createElement("h3");
        h3.innerHTML = data.entries[i].title;
        div.appendChild(h3);

        hr = document.createElement("hr");
        div.appendChild(hr)

        content = document.createElement("p");
        content.innerHTML = data.entries[i].content;
        div.appendChild(content);

        rss_container.appendChild(div);
    }
}

function parserss(url, callback) {

    $.ajax({
        url: document.location.protocol + '//ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=10&callback=?&q=' + encodeURIComponent(url),
        dataType: 'json',
        success: function(data) {
            callback(data.responseData.feed);
        }
    });
}

var getrss = function() {
    url=  'http://tech.163.com/special/000944OI/hulianwang.xml';
    url = 'http://feed.feedsky.com/matrix67';
    parserss(url, display_rss);
}

getrss()
