<?php
//sgwrite.php
//
//for redir url_rewrite_program ver. 1.0 (02.04.2016)
//Bekhterev Evgeniy jbe@mail.ru https://bekhterev.me 

//add url to temporary file 
file_put_contents("/usr/pbi/squid-amd64/share/warn/warned/$_POST[w_ip]", $_POST['w_url']."\r\n", FILE_APPEND | LOCK_EX);

//redirect with &w label
header("Location: $_POST[w_url]&w");
?>