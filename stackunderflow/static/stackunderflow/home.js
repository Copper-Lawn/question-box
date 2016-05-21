var $sorter = $('#sorter')
var $sort = $('#sort')
var $questions = $('#questions')
var question_list = $.get('/api/questions/')

var add_to_list = function(question) {
    var questionLink = $('<a href=/question/' + question.id + '>' + question.title.slice(0, 50) + '</a>');
    var $questionSummary = $('<div class=questionSummary>').appendTo($summary);
    questionLink.appendTo($questionSummary)
    $("<div class=questionText>").text(question.text.slice(0, 50) + "...").appendTo($questionSummary);
    displayKeywords(question, $questionSummary);
}


function displayKeywords(question, $questionSummary) {
    console.log("keywords:" + question.keywords)
    for (item in question.keywords) {
        console.log("item:" + item)
        if (item != 0) {
            $.get('/api/keywords/' + item, function(keyword) {
                keyword = keyword.keyword
                $('<div class=keyword>').text(keyword).appendTo($questionSummary)
            })
        }
    }
}


function getQuestions() {
    $.get('/api/questions/', {'sort': $sort.val()}, function(questions) {
        $('#questionsList').remove();
        $('<div id="questionsList">').appendTo($questions)
        questions.results.forEach(add_to_list)
        });
}


$sort.change( function() {
    getQuestions()
})

getQuestions();
