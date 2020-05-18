# Only run gftools qa on prs which contain font files.

# Find directories which contain files that have been altered or added. Also
# Skip /static directories.
CHANGED_DIRS=$(git diff origin/master HEAD --dirstat | sed "s/[0-9. ].*%//g" | grep -v "static")

for dir in $CHANGED_DIRS
do
    font_count=$(ls -1 $dir*.ttf 2>/dev/null | wc -l)
    if [ $font_count != 0 ]
    then
        echo $dir*.ttf
        gftools qa -f $dir*.ttf -gfb -a -o $(basename $dir)
    else
	echo "Skipping $dir. Dir is not a font family project"
    fi
done

