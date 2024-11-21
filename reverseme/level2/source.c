#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	no(void)
{
	puts("Nope.");
	exit(1);
}

int	ok(void)
{
	return (puts("Good job."));
}

typedef struct s_ascii_val
{
	char a;
	char b;
	char c;
	char d;
} ascii_val;


int	main(int argc, const char **argv, const char **envp)
{
	int				bytes_read;
	int				decoded_index;
	unsigned int	input_pos;
	int				decoded_length;
	int				is_valid_input;
	unsigned int	temp_pos;
	ascii_val		asc;
	char			user_input[24];
	char			decoded_key[9];
	int				digit_value;
	int				input_length;

	asc.d = '\0';
	printf("Please enter key: ");
	bytes_read = scanf("%23s", user_input);
	if (bytes_read != 1)
		no();
	if (user_input[0] != '0')
		no();
	if (user_input[1] != '0')
		no();
	fflush(stdin);
	memset(decoded_key, 0, sizeof(decoded_key));
	decoded_key[0] = 'd';
	decoded_index = 1;
	input_pos = 2;
	while (1)
	{
		decoded_length = strlen(decoded_key);
		temp_pos = input_pos;
		is_valid_input = 0;
		// Ensure we do not exceed the decoded key size and input length
		if (decoded_length < 8)
		{
			input_length = strlen(user_input);
			is_valid_input = temp_pos < input_length;
		}
		if (!is_valid_input)
			break ;
		// Read and convert three characters at a time
		asc.a = user_input[temp_pos];
		asc.b = user_input[temp_pos + 1];
		asc.c = user_input[temp_pos + 2];
		digit_value = atoi(&asc.a);
		decoded_key[decoded_index] = (char)digit_value;
		input_pos += 3;
		decoded_index++;
	}
	decoded_key[decoded_index] = '\0';
	// print decoded key
	// printf("%s\n", decoded_key);
	if (strcmp(decoded_key, "delabere") == 0)
		ok();
	else
		no();
	return (0);
}

int	xd(void)
{
	puts("Iii sapores crescit rei habetur disputo. An ab istud mo prius tanta error debet. Firma foret tes mea age capax sumne"
			". Ex ex ipsas actum culpa neque ab saepe. Existenti et principia co immittere probandam imaginari re mo. Quapropter "
			"industriam ibi cui dissimilem cucurbitas progressus perciperem. Essendi ratione si habetur gi ignotas cognitu nusqua"
			"m et.Sumpta vel uti obvium hoc tribuo libere. Egisse ingens hic sed inquam tamque rum gaudet aetate dat. Sum ignem j"
			"am ullas tur nexum vul. Divelli certius si errandi accipio colores de numerum. Is quavis tangam istius lumini essent"
			" vereor ab si. Aliam rea res tango vix simul certa certi.Imponere tractatu advenire ad superest occurret se quicquam"
			" si ha. Nihil solus pappo mo ei. Tum iis rom innata gloria hos quales. Ac sequentium im sufficeret institutum ad per"
			"mittere at. Aliquis aliarum quaenam at de totaque notitia ob exhibet. Simus tes sae sacra error. Neque nomen ac ad o"
			"pera is reges gi nobis. Se in objectivae ab is offerendum videbuntur satyriscos. Uno sequor tritam mediam essent eae"
			" usu rea. \t\t\tActum situs ideam solum uti signa mem. De ignotas errores gi remotam invenio suppono. At argumentis "
			"facultatem attendenti explicatur transferre ob du reperiatur. Gi du mali quod fuit an unum ei. Mea sperare ego senti"
			"at idearum spatium quaedam. Prius cur locus utrum hodie porro mente ope. Accepit liberam externo qui fal. \t\t\tVolu"
			"nt illico eas animus ita odores sacras ima. De ipsa vi ad deus alio ut deum. Acquiri aliquot in liquida vi maximam i"
			"s timenda. Ad aliquandiu ei facillimam repugnaret scripturas. Mearum imo namque falsae notatu hic mea non. Ero commu"
			"nibus exponantur hae sui quo virtutibus aliquandiu. \t\t\tNeque fieri horum errem ab me eo credo. Hanc sic meo quae "
			"ipsa. Fal membrorum existenti conservet per sapientia dubitavit. Apta gi de et enim gnum data. Id quadratam ut archi"
			"mede attingere re ne. Humanam infusum has iis veteris mei occasio replere istarum. Emanant poterit capaces at in num"
			"erum de exigere ob chartam. Cui tollitur periculi cau veniebat. Communibus vi at ut permittere ex progressum pauperr"
			"imi conflantur. Mentibus eo patiatur dependet et reliquis tenebras. Peccant ejusdem apertum et dicetur mo at. Ingeni"
			"osi exponetur sequentia si se. Affirmarem respondere desiderant ac vi quantumvis praecipuus se ex. Ob externis tanga"
			"tur existens recenseo ac. Una summam ens essent optime tempus firmum realis eos. Cetera fallat sic numero mei inquam"
			" rom ope revera. Causis humana fal verius ausint ope. Odor has alia otii dare ausi nunc quo agi. Praefatio du compon"
			"ant albedinem ad perlegere. Externarum ne si archimedes negationem. Praeditis scriptura antiquius cupientem ea nonnu"
			"llae recurrunt ad. Simile ut ne egisse animos fingam de. Scirem in coelum possim altera co");
	return puts("Author gi ex si im fallat istius. Refutent supposui qua sim nihilque. Me ob omni ideo gnum casu. Gi supersunt"
				" colligere inhaereat me sapientia is delaberer. Rom facillimam rem expectabam rum inchoandum mei. Apertum id "
				"suppono ac generis. Ab scio ad eo deus haud meae. Hominem ex vi ut remanet at quidnam. \t\t\tTunc ullo ut ann"
				"o poni voce de haud. Mallent prudens suo deumque qui sim invicem. Suum mo item inde de modi unde. Suo deo omn"
				"i quia opus. Co an habent inesse semper.Et innatas dominum cogitem sperare sopitum in. Substantia dei credidi"
				"sse vim iis excogitent exhibentur sub.");
}
int	xxd(void)
{
	puts("Iii sapores crescit rei habetur disputo. An ab istud mo prius tanta error debet. Firma foret tes mea age capax sumne"
			". Ex ex ipsas actum culpa neque ab saepe. Existenti et principia co immittere probandam imaginari re mo. Quapropter "
			"industriam ibi cui dissimilem cucurbitas progressus perciperem. Essendi ratione si habetur gi ignotas cognitu nusqua"
			"m et.Sumpta vel uti obvium hoc tribuo libere. Egisse ingens hic sed inquam tamque rum gaudet aetate dat. Sum ignem j"
			"am ullas tur nexum vul. Divelli certius si errandi accipio colores de numerum. Is quavis tangam istius lumini essent"
			" vereor ab si. Aliam rea res tango vix simul certa certi.Imponere tractatu advenire ad superest occurret se quicquam"
			" si ha. Nihil solus pappo mo ei. Tum iis rom innata gloria hos quales. Ac sequentium im sufficeret institutum ad per"
			"mittere at. Aliquis aliarum quaenam at de totaque notitia ob exhibet. Simus tes sae sacra error. Neque nomen ac ad o"
			"pera is reges gi nobis. Se in objectivae ab is offerendum videbuntur satyriscos. Uno sequor tritam mediam essent eae"
			" usu rea. \t\t\tActum situs ideam solum uti signa mem. De ignotas errores gi remotam invenio suppono. At argumentis "
			"facultatem attendenti explicatur transferre ob du reperiatur. Gi du mali quod fuit an unum ei. Mea sperare ego senti"
			"at idearum spatium quaedam. Prius cur locus utrum hodie porro mente ope. Accepit liberam externo qui fal. \t\t\tVolu"
			"nt illico eas animus ita odores sacras ima. De ipsa vi ad deus alio ut deum. Acquiri aliquot in liquida vi maximam i"
			"s timenda. Ad aliquandiu ei facillimam repugnaret scripturas. Mearum imo namque falsae notatu hic mea non. Ero commu"
			"nibus exponantur hae sui quo virtutibus aliquandiu. \t\t\tNeque fieri horum errem ab me eo credo. Hanc sic meo quae "
			"ipsa. Fal membrorum existenti conservet per sapientia dubitavit. Apta gi de et enim gnum data. Id quadratam ut archi"
			"mede attingere re ne. Humanam infusum has iis veteris mei occasio replere istarum. Emanant poterit capaces at in num"
			"erum de exigere ob chartam. Cui tollitur periculi cau veniebat. Communibus vi at ut permittere ex progressum pauperr"
			"imi conflantur. Mentibus eo patiatur dependet et reliquis tenebras. Peccant ejusdem apertum et dicetur mo at. Ingeni"
			"osi exponetur sequentia si se. Affirmarem respondere desiderant ac vi quantumvis praecipuus se ex. Ob externis tanga"
			"tur existens recenseo ac. Una summam ens essent optime tempus firmum realis eos. Cetera fallat sic numero mei inquam"
			" rom ope revera. Causis humana fal verius ausint ope. Odor has alia otii dare ausi nunc quo agi. Praefatio du compon"
			"ant albedinem ad perlegere. Externarum ne si archimedes negationem. Praeditis scriptura antiquius cupientem ea nonnu"
			"llae recurrunt ad. Simile ut ne egisse animos fingam de. Scirem in coelum possim altera co  ");
	return puts("Author gi ex si im fallat istius. Refutent supposui qua sim nihilque. Me ob omni ideo gnum casu. Gi supersunt"
				" colligere inhaereat me sapientia is delaberer. Rom facillimam rem expectabam rum inchoandum mei. Apertum id "
				"suppono ac generis. Ab scio ad eo deus haud meae. Hominem ex vi ut remanet at quidnam. \t\t\tTunc ullo ut ann"
				"o poni voce de haud. Mallent prudens suo deumque qui sim invicem. Suum mo item inde de modi unde. Suo deo omn"
				"i quia opus. Co an habent inesse semper.Et innatas dominum cogitem sperare sopitum in. Substantia dei credidi"
				"sse vim iis excogitent exhibentur sub.  ");
}

int	n(void)
{
	return (puts("Nope. "));
}

int	xxxd(void)
{
	puts("Iii sapores crescit rei habetur disputo. An ab istud mo prius tanta error debet. Firma foret tes mea age capax sumne"
			". Ex ex ipsas actum culpa neque ab saepe. Existenti et principia co immittere probandam imaginari re mo. Quapropter "
			"industriam ibi cui dissimilem cucurbitas progressus perciperem. Essendi ratione si habetur gi ignotas cognitu nusqua"
			"m et.Sumpta vel uti obvium hoc tribuo libere. Egisse ingens hic sed inquam tamque rum gaudet aetate dat. Sum ignem j"
			"am ullas tur nexum vul. Divelli certius si errandi accipio colores de numerum. Is quavis tangam istius lumini essent"
			" vereor ab si. Aliam rea res tango vix simul certa certi.Imponere tractatu advenire ad superest occurret se quicquam"
			" si ha. Nihil solus pappo mo ei. Tum iis rom innata gloria hos quales. Ac sequentium im sufficeret institutum ad per"
			"mittere at. Aliquis aliarum quaenam at de totaque notitia ob exhibet. Simus tes sae sacra error. Neque nomen ac ad o"
			"pera is reges gi nobis. Se in objectivae ab is offerendum videbuntur satyriscos. Uno sequor tritam mediam essent eae"
			" usu rea. \t\t\tActum situs ideam solum uti signa mem. De ignotas errores gi remotam invenio suppono. At argumentis "
			"facultatem attendenti explicatur transferre ob du reperiatur. Gi du mali quod fuit an unum ei. Mea sperare ego senti"
			"at idearum spatium quaedam. Prius cur locus utrum hodie porro mente ope. Accepit liberam externo qui fal. \t\t\tVolu"
			"nt illico eas animus ita odores sacras ima. De ipsa vi ad deus alio ut deum. Acquiri aliquot in liquida vi maximam i"
			"s timenda. Ad aliquandiu ei facillimam repugnaret scripturas. Mearum imo namque falsae notatu hic mea non. Ero commu"
			"nibus exponantur hae sui quo virtutibus aliquandiu. \t\t\tNeque fieri horum errem ab me eo credo. Hanc sic meo quae "
			"ipsa. Fal membrorum existenti conservet per sapientia dubitavit. Apta gi de et enim gnum data. Id quadratam ut archi"
			"mede attingere re ne. Humanam infusum has iis veteris mei occasio replere istarum. Emanant poterit capaces at in num"
			"erum de exigere ob chartam. Cui tollitur periculi cau veniebat. Communibus vi at ut permittere ex progressum pauperr"
			"imi conflantur. Mentibus eo patiatur dependet et reliquis tenebras. Peccant ejusdem apertum et dicetur mo at. Ingeni"
			"osi exponetur sequentia si se. Affirmarem respondere desiderant ac vi quantumvis praecipuus se ex. Ob externis tanga"
			"tur existens recenseo ac. Una summam ens essent optime tempus firmum realis eos. Cetera fallat sic numero mei inquam"
			" rom ope revera. Causis humana fal verius ausint ope. Odor has alia otii dare ausi nunc quo agi. Praefatio du compon"
			"ant albedinem ad perlegere. Externarum ne si archimedes negationem. Praeditis scriptura antiquius cupientem ea nonnu"
			"llae recurrunt ad. Simile ut ne egisse animos fingam de. Scirem in coelum possim altera co   ");
	return puts("Author gi ex si im fallat istius. Refutent supposui qua sim nihilque. Me ob omni ideo gnum casu. Gi supersunt"
				" colligere inhaereat me sapientia is delaberer. Rom facillimam rem expectabam rum inchoandum mei. Apertum id "
				"suppono ac generis. Ab scio ad eo deus haud meae. Hominem ex vi ut remanet at quidnam. \t\t\tTunc ullo ut ann"
				"o poni voce de haud. Mallent prudens suo deumque qui sim invicem. Suum mo item inde de modi unde. Suo deo omn"
				"i quia opus. Co an habent inesse semper.Et innatas dominum cogitem sperare sopitum in. Substantia dei credidi"
				"sse vim iis excogitent exhibentur sub.   ");
}

int	ww(void)
{
	puts("Good job. ");
	puts("Please entrer key: ");
	puts("%23s. ");
	puts("delabere. ");
	return (puts("%s, "));
}

int	xyxxd(void)
{
	puts("Iii sapores crescit rei habetur disputo. An ab istud mo prius tanta error debet. Firma foret tes mea age capax sumne"
			". Ex ex ipsas actum culpa neque ab saepe. Existenti et principia co immittere probandam imaginari re mo. Quapropter "
			"industriam ibi cui dissimilem cucurbitas progressus perciperem. Essendi ratione si habetur gi ignotas cognitu nusqua"
			"m et.Sumpta vel uti obvium hoc tribuo libere. Egisse ingens hic sed inquam tamque rum gaudet aetate dat. Sum ignem j"
			"am ullas tur nexum vul. Divelli certius si errandi accipio colores de numerum. Is quavis tangam istius lumini essent"
			" vereor ab si. Aliam rea res tango vix simul certa certi.Imponere tractatu advenire ad superest occurret se quicquam"
			" si ha. Nihil solus pappo mo ei. Tum iis rom innata gloria hos quales. Ac sequentium im sufficeret institutum ad per"
			"mittere at. Aliquis aliarum quaenam at de totaque notitia ob exhibet. Simus tes sae sacra error. Neque nomen ac ad o"
			"pera is reges gi nobis. Se in objectivae ab is offerendum videbuntur satyriscos. Uno sequor tritam mediam essent eae"
			" usu rea. \t\t\tActum situs ideam solum uti signa mem. De ignotas errores gi remotam invenio suppono. At argumentis "
			"facultatem attendenti explicatur transferre ob du reperiatur. Gi du mali quod fuit an unum ei. Mea sperare ego senti"
			"at idearum spatium quaedam. Prius cur locus utrum hodie porro mente ope. Accepit liberam externo qui fal. \t\t\tVolu"
			"nt illico eas animus ita odores sacras ima. De ipsa vi ad deus alio ut deum. Acquiri aliquot in liquida vi maximam i"
			"s timenda. Ad aliquandiu ei facillimam repugnaret scripturas. Mearum imo namque falsae notatu hic mea non. Ero commu"
			"nibus exponantur hae sui quo virtutibus aliquandiu. \t\t\tNeque fieri horum errem ab me eo credo. Hanc sic meo quae "
			"ipsa. Fal membrorum existenti conservet per sapientia dubitavit. Apta gi de et enim gnum data. Id quadratam ut archi"
			"mede attingere re ne. Humanam infusum has iis veteris mei occasio replere istarum. Emanant poterit capaces at in num"
			"erum de exigere ob chartam. Cui tollitur periculi cau veniebat. Communibus vi at ut permittere ex progressum pauperr"
			"imi conflantur. Mentibus eo patiatur dependet et reliquis tenebras. Peccant ejusdem apertum et dicetur mo at. Ingeni"
			"osi exponetur sequentia si se. Affirmarem respondere desiderant ac vi quantumvis praecipuus se ex. Ob externis tanga"
			"tur existens recenseo ac. Una summam ens essent optime tempus firmum realis eos. Cetera fallat sic numero mei inquam"
			" rom ope revera. Causis humana fal verius ausint ope. Odor has alia otii dare ausi nunc quo agi. Praefatio du compon"
			"ant albedinem ad perlegere. Externarum ne si archimedes negationem. Praeditis scriptura antiquius cupientem ea nonnu"
			"llae recurrunt ad. Simile ut ne egisse animos fingam de. Scirem in coelum possim altera co    ");
	return puts("Author gi ex si im fallat istius. Refutent supposui qua sim nihilque. Me ob omni ideo gnum casu. Gi supersunt"
				" colligere inhaereat me sapientia is delaberer. Rom facillimam rem expectabam rum inchoandum mei. Apertum id "
				"suppono ac generis. Ab scio ad eo deus haud meae. Hominem ex vi ut remanet at quidnam. \t\t\tTunc ullo ut ann"
				"o poni voce de haud. Mallent prudens suo deumque qui sim invicem. Suum mo item inde de modi unde. Suo deo omn"
				"i quia opus. Co an habent inesse semper.Et innatas dominum cogitem sperare sopitum in. Substantia dei credidi"
				"sse vim iis excogitent exhibentur sub.    ");
}