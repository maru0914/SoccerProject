$(document).ready(function () {
  lightbox.option({
    'wrapAround': true
  })

  $('.nav-button').click(function () {
    $('.nav-button').toggleClass('change');
  });

  $(window).scroll(function () {
    let position = $(this).scrollTop();
    if (position >= 200) {
      $('.nav-menu').addClass('custom-navbar');
    } else {
      $('.nav-menu').removeClass('custom-navbar');
    }
  });
  $(window).scroll(function () {
    let position = $(this).scrollTop();

    if (position >= 350) {
      $('.gallery').addClass('change');
    } else {
      $('.gallery').removeClass('change');
    }
  });
  $('[data-toggle="tooltip"]').tooltip();

  $('.gallery-list-item').click(function () {
    let value = $(this).attr('data-filter');
    if (value === 'all') {
      $('.filter').show(300);
    } else {
      $('.filter').not('.' + value).hide(300);
      $('.filter').filter('.' + value).show(300);
    }
  });

  $('.gallery-list-item').click(function () {
    $(this).addClass('active-item').siblings().removeClass('active-item');
  });

  $('tr').mouseover(function () {
    $(this).children('td.teamname').addClass('teamname-hover');
  });

  $('tr').mouseout(function () {
    $(this).children('td.teamname').removeClass('teamname-hover');
  });
});