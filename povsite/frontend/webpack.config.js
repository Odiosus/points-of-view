const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { watch } = require('fs');


module.exports = {
    watch: true,
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "/dist"),
        filename: "bundle.js"
    },
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude:/node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ]
    },
    stats: {
        children: true
    },
    plugins: [
        new HtmlWebpackPlugin({template: './dist/index.html'}),
        new MiniCssExtractPlugin(),
    ]
    }
