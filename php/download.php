<?php
ini_set('display_errors', 'On');
//���մ������Ĳ���
//python�ű�Ŀ¼
$script = dirname(dirname(__FILE__)) . '/download.py';
$output = array();
$cmd    = sprintf('python "%s"', $script);
exec($cmd, $output);
//���python���ص�����
echo '<pre>';
var_dump($output);
?>