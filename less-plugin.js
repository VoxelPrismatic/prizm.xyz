registerPlugin({
    install: function(less, pluginManager, functions) {
        functions.add('width', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "90vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "90vw";} // M580
            if ( w > 240 && w <= 360 ) {return "90vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "80vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "60vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "50vw";} // PC
            if (w > 1080 && w <= 1440) {return "40vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "40vw";} // 2K
            if (w > 2160 && w <= 3240) {return "40vw";} // 3K
            if (w > 3240 && w <= 4320) {return "40vw";} // 4K
            if (w > 4320 && w <= 5480) {return "40vw";} // 5K
            if (w > 5480 && w <= 8640) {return "40vw";} // 8K, and wow that is big
            return "30vw";
        });
        functions.add('fonts_code', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.2vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.2vw";} // M580
            if ( w > 240 && w <= 360 ) {return "3.2vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "3.2vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "1.5vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "1.5vw";} // PC
            if (w > 1080 && w <= 1440) {return "1.5vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "1.0vw";} // 2K
            if (w > 2160 && w <= 3240) {return "1.0vw";} // 3K
            if (w > 3240 && w <= 4320) {return "1.0vw";} // 4K
            if (w > 4320 && w <= 5480) {return "1.0vw";} // 5K
            if (w > 5480 && w <= 8640) {return "1.0vw";} // 8K, and wow that is big
            return "0.5vw";
        });
        functions.add('fonts_head', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "4.0vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "4.0vw";} // M580
            if ( w > 240 && w <= 360 ) {return "4.0vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "3.0vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "1.5vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "1.2vw";} // PC
            if (w > 1080 && w <= 1440) {return "1.0vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "1.0vw";} // 2K
            if (w > 2160 && w <= 3240) {return "1.0vw";} // 3K
            if (w > 3240 && w <= 4320) {return "1.0vw";} // 4K
            if (w > 4320 && w <= 5480) {return "1.0vw";} // 5K
            if (w > 5480 && w <= 8640) {return "1.0vw";} // 8K, and wow that is big
            return "1.0vw";
        });
        functions.add('fonts_cont', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.5vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.5vw";} // M580
            if ( w > 240 && w <= 360 ) {return "3.5vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "2.5vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "1.3vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "1.0vw";} // PC
            if (w > 1080 && w <= 1440) {return "0.8vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "0.5vw";} // 2K
            if (w > 2160 && w <= 3240) {return "0.5vw";} // 3K
            if (w > 3240 && w <= 4320) {return "0.5vw";} // 4K
            if (w > 4320 && w <= 5480) {return "0.5vw";} // 5K
            if (w > 5480 && w <= 8640) {return "0.5vw";} // 8K, and wow that is big
            return "0.5vw";
        });
        functions.add('fonts_warn', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.0vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.0vw";} // M580
            if ( w > 240 && w <= 360 ) {return "2.0vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "1.5vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "1.5vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "1.5vw";} // PC
            if (w > 1080 && w <= 1440) {return "1.0vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "1.0vw";} // 2K
            if (w > 2160 && w <= 3240) {return "1.0vw";} // 3K
            if (w > 3240 && w <= 4320) {return "1.0vw";} // 4K
            if (w > 4320 && w <= 5480) {return "1.0vw";} // 5K
            if (w > 5480 && w <= 8640) {return "1.0vw";} // 8K, and wow that is big
            return "1.0vw";
        });
        functions.add('fonts_foot', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.2vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.2vw";} // M580
            if ( w > 240 && w <= 360 ) {return "3.2vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "3.2vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "3.2vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "3.2vw";} // PC
            if (w > 1080 && w <= 1440) {return "3.2vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "3.2vw";} // 2K
            if (w > 2160 && w <= 3240) {return "3.2vw";} // 3K
            if (w > 3240 && w <= 4320) {return "3.2vw";} // 4K
            if (w > 4320 && w <= 5480) {return "3.2vw";} // 5K
            if (w > 5480 && w <= 8640) {return "3.2vw";} // 8K, and wow that is big
        });
        functions.add('fonts_sect', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.2vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.2vw";} // M580
            if ( w > 240 && w <= 360 ) {return "3.2vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "3.2vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "3.2vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "3.2vw";} // PC
            if (w > 1080 && w <= 1440) {return "3.2vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "3.2vw";} // 2K
            if (w > 2160 && w <= 3240) {return "3.2vw";} // 3K
            if (w > 3240 && w <= 4320) {return "3.2vw";} // 4K
            if (w > 4320 && w <= 5480) {return "3.2vw";} // 5K
            if (w > 5480 && w <= 8640) {return "3.2vw";} // 8K, and wow that is big
        });
        functions.add('fonts_clik', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.2vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.2vw";} // M580
            if ( w > 240 && w <= 360 ) {return "3.2vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "3.2vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "3.2vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "3.2vw";} // PC
            if (w > 1080 && w <= 1440) {return "3.2vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "3.2vw";} // 2K
            if (w > 2160 && w <= 3240) {return "3.2vw";} // 3K
            if (w > 3240 && w <= 4320) {return "3.2vw";} // 4K
            if (w > 4320 && w <= 5480) {return "3.2vw";} // 5K
            if (w > 5480 && w <= 8640) {return "3.2vw";} // 8K, and wow that is big
        });
        functions.add('fonts_link', function() {
            w = window.innerWidth;
            if (            w <= 160 ) {return "3.2vw";} // BRUH
            if ( w > 160 && w <= 240 ) {return "3.2vw";} // M580
            if ( w > 240 && w <= 360 ) {return "3.2vw";} // SMOL
            if ( w > 360 && w <= 640 ) {return "3.2vw";} // PHONE
            if ( w > 640 && w <= 720 ) {return "3.2vw";} // TABLET
            if ( w > 720 && w <= 1080) {return "3.2vw";} // PC
            if (w > 1080 && w <= 1440) {return "3.2vw";} // LARGE
            if (w > 1440 && w <= 2160) {return "3.2vw";} // 2K
            if (w > 2160 && w <= 3240) {return "3.2vw";} // 3K
            if (w > 3240 && w <= 4320) {return "3.2vw";} // 4K
            if (w > 4320 && w <= 5480) {return "3.2vw";} // 5K
            if (w > 5480 && w <= 8640) {return "3.2vw";} // 8K, and wow that is big
        });
    }
})
/*
@px: {
     bruh: 160px; m580: 240px; smol: 360px;
    phone: 640px;  tab: 720px;   pc: 1080px;
    large: 1440px; _2k: 2160px; _3k: 3240px;
      _4k: 4320px; _5k: 5480px; _8k: 8640px;
} @fonts_bruh: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_m580: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_smol: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_phone: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_tab: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_pc: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_large: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_2k: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_3k: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_4k: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_5k: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
} @fonts_8k: {
    code: 3.2vw; head: 4.0vw; cont: 3.5vw;
    warn: 3.0vw; foot: 2.5vw; sect: 2.5vw;
    clik: 3.5vw; link: 3.5vw;
}
*/
