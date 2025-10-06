$.ajax({
        url: 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=es-CL&page=1&primary_release_year=2025&sort_by=vote_average.desc&vote_count.gte=200&with_original_language=en',
        beforeSend: function(xhr) {
             xhr.setRequestHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYWQ2MDNkN2EyNTY4NWVlZDFmMTUzNWM1M2M2MmZkYyIsIm5iZiI6MTc1OTYwMzk2NC4yMzMsInN1YiI6IjY4ZTE2Y2ZjMzE5ZThmMTM0OTYxNzFjMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.I7_XZuPBQ_Q9cqqwEVTJM2Mr4w5gHEhsHTjCTcjpYZY"),
             xhr.setRequestHeader("accept", "application/json")
        }, success: function(data){
            alert(data);
            $.each(data.results, function(i, item){
		        $("#pelis").append("<div class=\"poster\"><img src='https://image.tmdb.org/t/p/w300_and_h450_bestv2"+item.poster_path+"'/></div>");
	});
        }
})