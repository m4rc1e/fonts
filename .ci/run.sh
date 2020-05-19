# Only run gftools qa on prs which contain font files.

# Find directories which contain files that have been altered or added. Also
# Skip /static directories.
CHANGED_DIRS=$(git diff origin/master HEAD --dirstat | sed "s/[0-9. ].*%//g" | grep -v "static")
OUT=out

for dir in $CHANGED_DIRS
do
    font_count=$(ls -1 $dir*.ttf 2>/dev/null | wc -l)
    if [ $font_count != 0 ]
    then
	echo "Checking $dir"
	mkdir -p $OUT
        gftools qa -f $dir*.ttf -gfb --fontbakery -o $OUT/$(basename $dir)_qa
    else
	echo "Skipping $dir. Directory does not contain fonts"
    fi
done

