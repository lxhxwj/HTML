<?php
ini_set('display_errors', 'On');
//接收传过来的参数
//python脚本目录
$script = dirname(dirname(__FILE__)) . '/download.py';
$output = array();
$cmd    = sprintf('python "%s"', $script);
exec($cmd, $output);
//输出python返回的数据
echo '<pre>';
var_dump($output);
?>