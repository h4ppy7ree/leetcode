<?php
/**
* File: /root-me/RFI/RFI_1_lang.php
* Project: leetcode
* Created Date: Monday, August 14th 2017, 10:03:40 am
* Author: yanyan.yyy
* -----
* Last Modified: 
* Modified By: 
* -----
*/

$filename = $_GET["fname"];
$handle = fopen($filename, "r");
$contents = fread($handle, filesize($filename));
fclose($handle);
echo $contents;

?>