if (!$) {
    $ = django.jQuery;
}



<script>
$(document).ready(function(){
  $("p").click(function(){
    $(this).hide();
  });
});
</script>