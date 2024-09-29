-- album_id	album_name	         artist_name	   album_year	genre	      label
-- 1	      After Hours	         The Weeknd	   2016	      R&B	      XO
-- 2	      Future Nostalgia	   Dua Lipa	      2022	      Pop	      Warner Records
-- 3	      Amigos	            Lady Gaga	   2020	      Dance-Pop	Interscope
-- 4	      Look Into The Future	Mac Miller	   2020	      Hip Hop	   Warner Records
-- 5	      Fine Line	         Harry Styles	2019	      Pop	      Columbia

with
  albums_2020 as (select * from music_albums where album_year = 2020)
select album_name from albums_2020 order by album_name;

+----------------------+
| ALBUM_NAME           |
|----------------------|
| Amigos               |
| Look Into The Future |
+----------------------+



with
   album_info_2020 as (select m.album_ID, m.album_name, b.band_name
      from music_albums as m inner join music_bands as b
      where m.band_id = b.band_id and album_year = 2020),
   Journey_album_info_2020 as (select *
      from album_info_2020 
      where band_name = 'Journey')
select album_name, band_name 
   from Journey_album_info_2020;
   
+----------------------+-----------+
| ALBUM_NAME           | BAND_NAME |
|----------------------+-----------|
| Look Into The Future | Journey   |
+----------------------+-----------+