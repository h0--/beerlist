<?php

putenv('LANG=en_US.UTF-8');

$output = "";

if (!isset($_GET['p'])) die;

$bar = $_GET['p'];

switch ($bar) {
	case 'mw':
	case 'op':
	case 'craft':
	case 'jbm':
	case 'fa':
		$update = "./tools/update_cache.sh ".$bar;
		$file = "cache/".$bar.".json";
		break;
	case 'history':
		die("<pre>".shell_exec("(cat ./log/beerlog.json | ./tools/log2table.py)")."</pre>");
		break;
	default:
		die("'mw', 'op', 'craft' or 'history'\n");
}

// Handle caching
$modtime = filemtime($file);
$curtime = time();

if ($curtime > $modtime + 300) {
	shell_exec($update);
}

// Read cached file
$output = shell_exec("(cat ".$file." | ./tools/json2table.py)");
$titles = shell_exec("(cat ".$file." | ./tools/json2titles.py)");

// For browsers
if (stripos($_SERVER['HTTP_USER_AGENT'], "Mozilla") !== false) {
	print "<head><title>".$titles."</title></head>\n";
	$output = "<pre>".$output."</pre>";
}

// Short version for IRC
if (isset($_GET['t']) && $_GET['t'] == "irc") {
	print($titles);
} else {
	print($output);
}
?>
