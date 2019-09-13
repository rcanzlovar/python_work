
<form<!DOCTYPE html>
<html>
    <head>
        <title>MovieList</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="description" content="Movie List Searcher">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
        <style type="text/css">
    .button {
        background-color: #4CCF50;
        color: white;
        padding: 5px 3px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 11px;
         border-radius: 6px
        margin: 4px 2px;
        cursor: pointer;
    }
    /* audio */
    .btn_mp3 {
        color: red;
        background-color: green;
    }
    .btn_m4a {
        color: orange;
        background-color: blue;
    }
    // video
    .btn_avi {
        color: red;
        background-color: green;
    }
    .btn_mkv {
        color: red;
        background-color: green;
    }
    /* ebook related */
    .btn_epub {
        color: red;
        background-color: green;
    }
    .btn_mobi {
        color: orange;
        background-color: aquamarine;
    }
    .btn_pdf {
        color: white;
        background-color: red;
    }
    </style>
  </head>
    
  



    <body>
        <h1>Media Library Check</h1>
        <p>Type the title to search</p>
<?php
    show_form();
        
    $DEBUG = TRUE;
   $DEBUG = FALSE;
   if (isset($_POST['counter'])) {
       $counter = $_POST['counter'];
   } else {
       $counter = 20;
   }



    # what did we pass? 
    if ($DEBUG) { _show_cgi(); }
#######################################3
    if (array_key_exists('term', $_POST)) {
        $term = $_POST['term'];
        $term = str_replace(' ', '.', $term);

        $filelist = glob("./*.txt");
        
        if ($DEBUG) { print_r ($filelist); }

        foreach ($filelist as $file) {
            /*
            echo "STRPOS ",
                $_POST['mediatype'],
                ' ',
                $file,
                ' ',
                strpos($file,$_POST['mediatype']),
                '<br />';
                */

                # but are they the right kind of people?
            if (strpos($file,'.txt') > 0 && 
                strpos($file,$_POST['mediatype']) == 2) {
                echo "<h2> $file </h2> ";
                searchfile($file,$term);
            }
        }


#$stream = new SplFileObject($file); 
#$grepped = new RegexIterator($stream, $term); 

#           $file = file_get_contents ('./md5list.txt');
#foreach ($grepped as $line) {
#    echo $line;
#}
#                $file = file_get_contents ('./md5list.txt');
#                preg_match_all ($_GET['term'], $file, $matches);
    }

#######################################3
function _show_cgi() {
    echo "_show_cgi:";
    # these lines show all the post and get things
    foreach (array('get' => $_GET, 'post' => $_POST) as $type => $values) {

        foreach ($values as $key => $value) {
                echo "$type: $key =>  $value<br />\n";
        }
    }
    print_r($_POST); 
}
#######################################3
function show_form() {
    global $DEBUG;
    if ($DEBUG) { echo "DEBUG $DEBUG EVEN MO<br />\n"; }
    echo 
'<form action="index1.php" method="post">';


echo '<input type="text" name="term" ';
if (isset($_POST['term']) 
    && $_POST['term'] != '') { 
    echo ' value="',
        $_POST['term'],'" ';
    }
echo 
'/> <input type="submit" class="button" value="Look" id="look">
<br />'; 

echo '<input type="radio" name="mediatype" value="video" ';
echo (isset($_POST['mediatype']) && ($_POST['mediatype'] == 'video')) 
    ? 'checked' : '';
echo "> Video";

echo '<input type="radio" name="mediatype" value="audio" ';
echo (isset($_POST['mediatype']) && ($_POST['mediatype'] == 'audio')) 
    ? 'checked' : '';
echo "> Audio";

echo '<input type="radio" name="mediatype" value="ebook" ';
echo (isset($_POST['mediatype']) && ($_POST['mediatype'] == 'ebook')) 
    ? 'checked' : '';
echo "> ebook";

echo '<br />';

echo ' Return 
<select name="counter">
  <option value="6">5</option>
  <option value="21" selected>20</option>
  <option value="51">50</option>
  <option value="101">100</option>
  <option value="0">Unlimited</option>
</select> results.
</form>';


}
#######################################3
function searchfile ($file,$searchstring) {
        # use this way so we don't have the whole
        # file in memory at once
    global $DEBUG;
    global $counter;

    if ($DEBUG) { 
        echo " file $file<br /> searchsring $searchstring <br />"; 
    }

    # split the file into lines:
    $parts = new SplFileObject($file);
    # iterate over the file... 
    foreach ($parts as $line) {
        if (strpos($line,'.jpg')) {
            continue;
 #       } else if (strpos($line,'Thumbs.db')) {
 #           continue;
        } else if (strpos($line,'.srt')) {
            continue;
        } else if (strpos($line,'.db')) {
            continue;
        } else if (strpos($line,'.URL')) {
            continue;
        } else if (strpos($line,'.url')) {
            continue;
        } else if (strpos($line,'.opf')) {
            continue;
        } else if (strpos($line,'desktop.ini')) {
            continue;
        } else if (strpos($line,'DS_Store')) {
            continue;
        } else if (strpos($line,'@')) {
            continue;
        } else if  ( preg_match ('/'.$searchstring.'/i', $line)) {
            pretty_print ($line);
        }
    }

}

#######################################3
function pretty_print ($item) {
    global $counter;
    $counter--; 
    if ($counter == 1) { exit; }
#        echo "<p>COUNTER $counter</p>\n";
    $matches = [];
#1d9accd9b67157b58890bafec38f2a5e
    preg_match('/^([0-9a-fA-F]{32}) (.*)/', $item,$matches);
        # $matches[0] has the whole line, 
        # $matches[1] has the checksum 
        # $matches[2] has the full path 
    echo "\n<!-- MATCHES2 ",$item," -->";

    $elements = explode('/',$matches[2]);
        # print_audio($elements)

    switch ($_POST['mediatype']) {
        case 'video':
            print_video ($elements);
            break;
        case 'ebook':
            print_ebook ($elements);
            break;
        case 'audio':
            print_audio ($elements);
            break;
        default:
            print_audio ($line);
            break;
    }
}
#######################################3
function print_tv ($elementarray) {

    echo "<h4>tv show", 
         $elementarray[count($elementarray)-4],'<br />',
         $elementarray[count($elementarray)-3],'<br />',
         $elementarray[count($elementarray)-2],'<br />',
         $elementarray[count($elementarray)-1];


}
#######################################3
$oldmoviegenre = '';
function print_video ($elementarray) {
##    echo "<br />tv?",$elementarray[count($elementarray)-4];
    echo strpos('TV', $elementarray[count($elementarray)-4]);
    if (strpos('TV', $elementarray[count($elementarray)-4])) {
        print_tv($elementarray);
        return;
    }
    global $oldmoviegenre;
    $genre = $elementarray[count($elementarray)-3];
    $movie = $elementarray[count($elementarray)-1];
    echo   get_extension($movie);
    $bits = explode('.',$movie);
    if (isset($bits[1])) {
        # this turns out to be the year
#        echo 
#            ($genre == $oldmoviegenre) ?  " " : '<em>'.$genre.'<em>';

#        echo "bits1 $bits[1]"; # extension
        echo "<em>genre $genre</em> <strong>$bits[0]</strong>";
        echo "<br />";
        $oldmoviegenre = $genre;
    }
}
#######################################3
function print_ebook ($elementarray) {
#    print_r($elementarray);
    $book = $elementarray[count($elementarray)-1];
    $description = $elementarray[count($elementarray)-2];
    echo   get_extension($book);


    $bits = explode('-',$book);
    echo "<strong>" . $bits[0] . "</strong>";
    echo "<em>" 
        . (isset($bits[1])? $bits[1] : " ") 
        . "</em><br />" 
        . $description;
    echo "<br />";
}
#######################################3
function get_extension($string) {

    $bits1 = explode('.',$string);
    $extension = '';

    # extension is always the same place to calculate?
    if (count($bits1) != 1) {

        $extension = $bits1[count($bits1)-1];
        return '<button class="button">'.$extension.'</button>';
    } else {
        return "";
    }
}
#######################################3
# establish these outside the function for persistence
$oldartist = "";
$oldalbum = "";
function print_audio ($elementarray) {
    global $oldartist;
    global $oldalbum;

        # music/a/abcartist/aaalbum/song.mp3
        if (strlen($elementarray[count($elementarray)-3] == 1)) {
            echo "case -4";
            $artist = $elementarray[count($elementarray)-3];
            $album = $elementarray[count($elementarray)-2];
#            $album = " ";
        } else if (strlen($elementarray[count($elementarray)-2] == 1)) {
            echo "case -3";
        # music/a/abcartist/song.mp3
            $artist = $elementarray[count($elementarray)-2];
            $album = "";
        } else {
            $artist = $elementarray[count($elementarray)-3];
            $album = $elementarray[count($elementarray)-2];
        }

        # by putting the formatting tags here, we can 
        # compare later
#        if (($artist != '') || ($album != '')) {

        if (($artist != $oldartist) || ($album != $oldalbum)) {
            echo "<h3>",
                ($artist == $oldartist) 
                    ?  '' 
                    : '<strong>'.$artist.'</strong> ',
                (($album == $oldalbum) || (strpos('nknown',$album))) 
                    ?  '' 
                    : '<em>'.$album.'</em>',
                '</h3>';
        }


        # Now.. about that song... 
            $song = $elementarray[count($elementarray)-1];
        $bits = explode('.',$song);
        $extension = $bits[count($bits)-1];

#        $extension = get_extension($song);
        $songtitle = basename($song, $extension).PHP_EOL;

echo "<br />",get_extension( $song);
#    $songtitle,"<br />";


        if (count($bits) > 1) {
            # if there are more than 1, then we may
            # have a period in the file name. Get rid
            # of the last thing, and then push it all 
            # back togethe/h2uur
            unset($bits[count($bits)-1]);
            $songtitle = join($bits,'.');
        } else if (isset($bits[1])) {
            # else we have just the name in one
            # cell
            $songtitle = $bits[0];
        }

        echo " <strong>$songtitle</strong>";
        # set this for the next go-round
        $oldartist = $artist;
        $oldalbum = $album;
    }
         ?>

        <script type="text/javascript"></script>


    </body>
</html>
