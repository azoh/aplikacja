$(document).ready(function() {
    $('.field-status').each(function(index, element) {
        var element = $(element);
        switch (element.text()) {
            case "Zgłoszona":
                element.addClass('add');
            break;
            case "Usunięta":
                element.addClass('done');
            break;
            case "Rozpoczęta":
                element.addClass('wait');
            break;
<<<<<<< HEAD
            case "Oczekuje na części":
                element.addClass('waiting');
=======
/*
            case "Oczekuje na części":
                element.addClass('warning');
>>>>>>> 556f831d51cf04fbbe0971ad94f91c591eaf24c1
            break;
            case "Zlecona na zewnątrz":
                element.addClass('outsourced');
            break;
            case "Nienaprawialna":
                element.addClass('irreparable');
            break;
<<<<<<< HEAD
=======
*/
>>>>>>> 556f831d51cf04fbbe0971ad94f91c591eaf24c1
        }
    });
});
