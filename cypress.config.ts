import {defineConfig} from "cypress";

export default defineConfig({
    reporter: "mochawesome",
    reporterOptions: {
        charts: true,
        overwrite: false,
        html: false,
        json: true,
        reportDir: "cypress/report/mochawesome-report"
    },
    chromeWebSecurity: false,
    e2e: {
        supportFile: false,
        experimentalRunAllSpecs: true
    },
});
