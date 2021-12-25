function myvalidation() {
    var flag = true;
    input = document.getElementsByTagName("input");
    span = document.getElementById("span");
    span1 = document.getElementById("span1");

    if (input[1].value.length < 3) {
        input[1].style.borderColor = "red";
        span.style.color = "red";
        span.innerHTML = "At least 4 words"
        flag = false;
    }
    else {
        input[1].style.borderColor = "green";
        span.innerHTML = ""
    }

    if (input[2].value.length < 6) {
        input[2].style.borderColor = "red";
        span1.style.color = "red";
        span1.innerHTML = "At least 7 words"
        flag = false;
    }

    else {
        input[2].style.borderColor = "green";
        span1.innerHTML = ""
    }
    return flag
}

function remove_error_msg(e) {
    if (e.value.length == 3) {
        document.getElementById("span").innerHTML = "";
        document.getElementsByTagName("input").style.borderColor = "green";
    }

    else {
        document.getElementById("span").innerHTML = "At least 4 words";
    }

    if (e.value.length == 6) {
        document.getElementById("span1").innerHTML = "";
        document.getElementsByTagName("input").style.borderColor = "green";
    }

    else {
        document.getElementById("span1").innerHTML = "At least 7 words";
    }


}